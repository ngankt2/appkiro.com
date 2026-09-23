#!/usr/bin/env python3
"""Validate the separate stable update channel for each desktop app."""
import argparse
import base64
from datetime import datetime
import json
from pathlib import Path
import re
from urllib.parse import urlparse

REPOSITORY = "ngankt2/appkiro.com"
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
VERSION = re.compile(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)")
PLATFORM = re.compile(r"(?:darwin|windows|linux)-(?:aarch64|x86_64|i686|armv7)(?:-(?:nsis|msi|appimage))?")
ASSET = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*")


def version_tuple(version):
    if not isinstance(version, str) or not VERSION.fullmatch(version):
        raise ValueError("Stable versions must use MAJOR.MINOR.PATCH without a v prefix")
    return tuple(map(int, version.split(".")))


def validate_manifest(app, data, allow_empty=True):
    if not SLUG.fullmatch(app):
        raise ValueError("Invalid app slug")
    if not isinstance(data, dict):
        raise ValueError("Manifest must be an object")
    version = data.get("version")
    version_tuple(version)
    if not isinstance(data.get("notes", ""), str):
        raise ValueError("Release notes must be text")
    platforms = data.get("platforms")
    if not isinstance(platforms, dict):
        raise ValueError("platforms must be an object")
    if not platforms:
        if allow_empty and version == "0.0.0":
            return []
        raise ValueError("A published release needs at least one platform")
    if version == "0.0.0":
        raise ValueError("0.0.0 is reserved for an unpublished channel")
    date = data.get("pub_date", "")
    try:
        if not isinstance(date, str) or datetime.fromisoformat(date.replace("Z", "+00:00")).tzinfo is None:
            raise ValueError()
    except ValueError:
        raise ValueError("pub_date must be a timezone-aware ISO 8601 timestamp") from None
    assets = []
    for platform, entry in platforms.items():
        if not PLATFORM.fullmatch(platform) or not isinstance(entry, dict):
            raise ValueError(f"Invalid platform: {platform}")
        url = urlparse(entry.get("url", ""))
        filename = url.path.rsplit("/", 1)[-1]
        expected = f"/{REPOSITORY}/releases/download/{app}-v{version}/{filename}"
        if (url.scheme != "https" or url.netloc != "github.com" or url.path != expected
                or url.query or url.fragment or not ASSET.fullmatch(filename)):
            raise ValueError(f"{platform}: URL must target this app's exact versioned release")
        suffixes = (".app.tar.gz",) if platform.startswith("darwin-") else ((".exe", ".msi") if platform.startswith("windows-") else (".AppImage",))
        if not filename.endswith(suffixes):
            raise ValueError(f"{platform}: not an updater payload for this platform")
        if platform.endswith("-nsis") and not filename.endswith(".exe"):
            raise ValueError("NSIS platforms need an .exe payload")
        if platform.endswith("-msi") and not filename.endswith(".msi"):
            raise ValueError("MSI platforms need an .msi payload")
        signature = entry.get("signature")
        try:
            lines = base64.b64decode(signature, validate=True).decode("utf-8").splitlines()
            if len(lines) != 4 or not lines[0].startswith("untrusted comment:") or not lines[2].startswith("trusted comment:"):
                raise ValueError()
            packet = base64.b64decode(lines[1], validate=True)
            global_signature = base64.b64decode(lines[3], validate=True)
            if len(packet) != 74 or packet[:2] not in (b"Ed", b"ED") or len(global_signature) != 64:
                raise ValueError()
        except (ValueError, TypeError, UnicodeDecodeError):
            raise ValueError(f"{platform}: signature must contain a Tauri .sig file, not its path") from None
        assets.append(filename)
    return sorted(set(assets))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    args = parser.parse_args()
    paths = args.paths or sorted((Path(__file__).resolve().parents[1] / "updates").glob("*/latest.json"))
    if not paths:
        raise ValueError("No app update manifests found")
    for path in paths:
        validate_manifest(path.parent.name, json.loads(path.read_text()))
        print(f"Valid: {path.parent.name}/{path.name}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit(str(error)) from error
