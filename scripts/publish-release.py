#!/usr/bin/env python3
"""Publish prepared release assets, then advance only that app's update channel."""
import argparse
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validation", ROOT / "scripts/validate-updates.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


def run(*args, check=True):
    return subprocess.run(args, cwd=ROOT, check=check, capture_output=True, text=True)


def verify_identity(message):
    forbidden = re.compile(r"codex|openai|chatgpt|co-authored-by|generated-by|assisted-by|ai assistance|automated generation", re.I)
    identities = [run("git", "var", key).stdout.strip() for key in ("GIT_AUTHOR_IDENT", "GIT_COMMITTER_IDENT")]
    if any(forbidden.search(text) for text in [message, *identities]):
        raise ValueError("Commit identity or message contains a prohibited attribution marker")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("app")
    parser.add_argument("artifacts", type=Path)
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args()
    folder = args.artifacts.resolve()
    data = json.loads((folder / "latest.json").read_text())
    filenames = validation.validate_manifest(args.app, data, allow_empty=False)
    channel = ROOT / "updates" / args.app / "latest.json"
    current = json.loads(channel.read_text())
    if validation.version_tuple(data["version"]) <= validation.version_tuple(current["version"]):
        raise ValueError("The release version must be newer than the current app channel")
    assets = {"latest.json"}
    for filename in filenames:
        payload, signature = folder / filename, folder / (filename + ".sig")
        if not payload.is_file() or payload.is_symlink() or payload.stat().st_size == 0:
            raise ValueError(f"Missing payload: {filename}")
        for entry in data["platforms"].values():
            if entry["url"].endswith("/" + filename) and signature.read_text().strip() != entry["signature"]:
                raise ValueError(f"Signature file disagrees with manifest: {filename}")
        assets.update([filename, signature.name])
    # Installers are optional; source archives, keys, and arbitrary files are never uploaded.
    for path in folder.iterdir():
        if path.is_file() and not path.is_symlink() and path.name.endswith((".dmg", ".exe", ".msi")):
            if data["version"] not in path.name or not validation.ASSET.fullmatch(path.name) or "local" in path.name.lower():
                raise ValueError(f"Installer must be versioned and ready for public distribution: {path.name}")
            assets.add(path.name)
    tag = f'{args.app}-v{data["version"]}'
    message = f'Publish {args.app} {data["version"]} update channel'
    print(f"Repository: {validation.REPOSITORY}\nRelease: {tag}\nChannel: updates/{args.app}/latest.json")
    print("Assets:\n" + "\n".join(f"  {name}" for name in sorted(assets)))
    if not args.publish:
        print("Dry run. Pass --publish after reviewing these artifacts.")
        return
    if run("git", "status", "--porcelain").stdout.strip():
        raise ValueError("Start from a clean checkout before publishing")
    if run("git", "branch", "--show-current").stdout.strip() != "main":
        raise ValueError("Publish from the main branch")
    remote = run("git", "remote", "get-url", "origin").stdout.strip()
    if remote not in (f"git@github.com:{validation.REPOSITORY}.git", f"https://github.com/{validation.REPOSITORY}.git"):
        raise ValueError("origin must point to the configured release repository")
    verify_identity(message)
    run("git", "fetch", "origin", "main")
    if run("git", "rev-parse", "HEAD").stdout != run("git", "rev-parse", "origin/main").stdout:
        raise ValueError("Sync main with origin/main before publishing")
    run("gh", "auth", "status")
    existing = run("gh", "release", "view", tag, "--repo", validation.REPOSITORY, check=False)
    if existing.returncode == 0:
        raise ValueError("That release already exists; preserve it and use a new patch version")
    # The body lives in a file to preserve literal text and newlines.
    import tempfile
    with tempfile.TemporaryDirectory(prefix="appkiro-release-") as temporary:
        notes = Path(temporary) / "notes.md"
        notes.write_text(data.get("notes", ""))
        run("gh", "release", "create", tag, "--repo", validation.REPOSITORY, "--target", "main",
            "--title", f'{args.app} {data["version"]}', "--notes-file", str(notes), "--draft")
    run("gh", "release", "upload", tag, "--repo", validation.REPOSITORY,
        *[str(folder / filename) for filename in sorted(assets)])
    run("gh", "release", "edit", tag, "--repo", validation.REPOSITORY, "--draft=false", "--latest=false")
    shutil.copyfile(folder / "latest.json", channel)
    run("git", "add", "--", str(channel.relative_to(ROOT)))
    verify_identity(message)
    run("git", "commit", "-m", message)
    run("git", "push", "origin", "main")
    print(f"Published https://github.com/{validation.REPOSITORY}/releases/tag/{tag}")


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as error:
        raise SystemExit(error.stderr.strip() or "A release command failed") from error
    except (ValueError, OSError) as error:
        raise SystemExit(str(error)) from error
