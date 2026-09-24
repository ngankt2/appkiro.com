# Desktop app releases

[Appkiro website](https://appkiro.com) · [App catalog](../apps/README.md)

This repository hosts public installers and update manifests for multiple apps. Application source code and private signing keys belong outside this repository.

See the [app catalog](../apps/README.md) for product introductions, features, current downloads, and release notes.

| App | Update manifest | Release tags |
| --- | --- | --- |
| [AgentProfiles](../apps/agentprofiles/README.md) | [`agentprofiles/latest.json`](agentprofiles/latest.json) | `agentprofiles-v<version>` |
| [Kiro Password Manager](../apps/appkiro-password-manager/README.md) | [`appkiro-password-manager/latest.json`](appkiro-password-manager/latest.json) | `appkiro-password-manager-v<version>` |

The stable AgentProfiles endpoint is:

```text
https://raw.githubusercontent.com/ngankt2/appkiro.com/main/updates/agentprofiles/latest.json
```

Each app has its own directory, release tag prefix, and signing key. Do not point apps at `releases/latest/download/latest.json`: the repository contains releases for different products. Use immutable, versioned release asset URLs inside each manifest.

## Register an app

1. Choose a lowercase slug, for example `myapp`.
2. Create `updates/myapp/latest.json`, initially `{"version":"0.0.0","notes":"No release published yet.","platforms":{}}`.
3. Add the public updater key as `updates/myapp/updater.pub`. Keep its private counterpart in protected local storage or private build secrets. Never rotate the key without first delivering a migration to existing installations.
4. Configure the app to check its own raw manifest URL and verify updates against that public key.
5. Add the app to the table above.

An empty platform map deliberately announces no installable update. AgentProfiles displays “No update has been published for this platform yet.” Older binaries without an updater need one manual installation of the first updater-enabled release.

## Publish an update

Build and test in the private source workspace. Prepare an artifact directory containing `latest.json`, signed updater payloads, their `.sig` files, and optional installers. The manifest must list only platforms actually built and tested. macOS universal payloads can be listed for both `darwin-aarch64` and `darwin-x86_64`; Windows can use `windows-x86_64-nsis` and/or `windows-x86_64-msi` to match the installed bundle type.

The publisher uses your existing Git identity and GitHub CLI login. Start from a clean `main` checkout of this repository:

```bash
python3 scripts/validate-updates.py
python3 scripts/publish-release.py agentprofiles /absolute/path/to/release-artifacts
# Review the asset list, then publish:
python3 scripts/publish-release.py agentprofiles /absolute/path/to/release-artifacts --publish
```

The default is a dry run. Publishing creates a draft release with a product-specific tag, uploads the payloads, publishes it without changing the repository-wide “latest” release, then commits and pushes only that app's manifest. Other apps' channels are untouched. It refuses an existing release tag and never replaces prior artifacts. If the final manifest push fails, the release exists but clients remain on the previous channel until the manifest commit is pushed.

After the release assets are available, update the current version, download links, and release notes in `apps/<app>/README.md`, and update the version listed in `apps/README.md`. Write app overviews, README files, release notes, and installation instructions in clear, professional English. Include a visible link to https://appkiro.com in each app README and in the release documentation.

The publisher checks manifest structure, product namespace, version increases, payload filenames, and matching signature files. The app performs cryptographic verification before installation. Release assets must be signed and tested by the private build process before publishing; macOS public distribution also needs Developer ID signing and Apple notarization.

GitHub may cache raw manifests for a few minutes. No GitHub token is bundled with an app; installers and update metadata are publicly downloadable.
