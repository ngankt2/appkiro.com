#!/usr/bin/env python3
"""Update documentation for the existing Kiro Password Manager 1.0.17 release."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "release-assets"
REPOSITORY = "ngankt2/appkiro.com"
APP = "appkiro-password-manager"
VERSION = "1.0.17"
TAG = f"{APP}-v{VERSION}"
ARCHIVE = f"KiroPasswordManager_{VERSION}_arm64.app.tar.gz"
APPLICATION_FILES = (ARCHIVE, ARCHIVE + ".sig")
DOCUMENTATION_FILES = ("README.txt", "BUILD-INFO.json", "latest.json", "SHA256SUMS")


def run(*args):
    return subprocess.run(args, cwd=ROOT, check=True, capture_output=True, text=True).stdout


def release():
    return json.loads(run("gh", "api", f"repos/{REPOSITORY}/releases/tags/{TAG}"))


def verify_assets(published, names):
    if published["tag_name"] != TAG or published["draft"]:
        raise ValueError("The expected published release is not available")
    remote = {asset["name"]: asset for asset in published["assets"]}
    for name in names:
        local = (ASSETS / name).read_bytes()
        expected = "sha256:" + hashlib.sha256(local).hexdigest()
        if name not in remote or remote[name]["size"] != len(local) or remote[name].get("digest") != expected:
            raise ValueError(f"Published asset does not match the local file: {name}")


def main():
    spec = importlib.util.spec_from_file_location("validation", ROOT / "scripts/validate-updates.py")
    validation = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(validation)
    manifest = json.loads((ASSETS / "latest.json").read_text())
    if manifest["version"] != VERSION:
        raise ValueError("This workflow only updates documentation for version 1.0.17")
    validation.validate_manifest(APP, manifest, allow_empty=False)
    if manifest["platforms"]["darwin-aarch64"]["signature"] != (ASSETS / (ARCHIVE + ".sig")).read_text().strip():
        raise ValueError("The manifest signature differs from the existing package signature")
    notes = (ASSETS / "RELEASE-NOTES.md").read_text()
    if manifest["notes"] != notes or "https://appkiro.com" not in notes:
        raise ValueError("Release notes and website links must be consistent")
    before = release()
    verify_assets(before, APPLICATION_FILES)
    # Upload only documentation and metadata; the application and its signature stay intact.
    run("gh", "release", "upload", TAG, "--repo", REPOSITORY, "--clobber",
        *[str(ASSETS / name) for name in DOCUMENTATION_FILES])
    run("gh", "release", "edit", TAG, "--repo", REPOSITORY,
        "--notes-file", str(ASSETS / "RELEASE-NOTES.md"), "--latest=false")
    after = release()
    verify_assets(after, (*APPLICATION_FILES, *DOCUMENTATION_FILES))
    if after["body"].strip() != notes.strip() or after["prerelease"] != before["prerelease"]:
        raise ValueError("Release documentation or release status differs after the update")
    print(f"Updated and verified documentation: {after['html_url']}")


if __name__ == "__main__":
    main()
