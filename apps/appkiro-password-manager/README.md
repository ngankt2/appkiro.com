# Kiro Password Manager

[App catalog](../README.md) · [Appkiro website](https://appkiro.com)

Kiro Password Manager stores passwords and account details in encrypted vaults on your device. Create a vault with a master password, organize entries with folders and tags, and search, view, or edit accounts in one place.

Vaults are stored as encrypted `.akpr` files. No online account is required. Network connections are used to check for updates and download icons or website favicons when requested.

## Features

- Manage passwords, notes, API credentials, environment variables, and custom fields.
- Organize entries with folders, tags, and favorites. Select a tag badge in the sidebar to filter accounts.
- Generate passwords, view TOTP codes, and reveal part of a password with a different masking pattern each time.
- Choose a bundled brand or bank logo, an image URL, or a website favicon. Images are cached in the encrypted vault until you replace the image or icon.
- See when each account was last updated on the right side of its row.
- Review edit history, create automatic or manual backups, restore data, and export encrypted vaults.
- Import KeePass `.kdbx` data with a preview before creating a new vault.
- Automatically lock vaults, limit how long passwords remain visible, and clear secrets copied by the app.

## Download and installation

| Detail | Current release |
| --- | --- |
| Version | **1.0.17** |
| Operating system | macOS 13 or later |
| Architecture | Apple Silicon (arm64) |
| Release status | Early access, ad hoc signed, not notarized |

**[Download Kiro Password Manager 1.0.17 for macOS (.app.tar.gz)](https://github.com/ngankt2/appkiro.com/releases/download/appkiro-password-manager-v1.0.17/KiroPasswordManager_1.0.17_arm64.app.tar.gz)**

1. Extract the downloaded archive to get `Kiro Password Manager.app`.
2. Move the app into Applications.
3. Quit any older instance, then open the new app.

## What's new in 1.0.17

- Use the **Kiro Password Manager** product name throughout the interface.
- Filter accounts by tags in the sidebar and reuse cached icons and favicons.
- Choose from an expanded logo catalog, including WeChat, Messenger, and major international banks, with readable labels in smaller windows.
- Display each account's last update on the right: `HH:mm` for today, `dd/MM` for other dates in the current year, and `dd/MM/yyyy` for dates in other years.
- Randomize the concealed positions each time partial password preview is used.

Check for updates from Settings, the app menu, or the version number in the footer. The app also checks at startup and every six hours while visible. You choose when to download, install, and restart.

| Update resource | Link |
| --- | --- |
| Current release | [Kiro Password Manager 1.0.17](https://github.com/ngankt2/appkiro.com/releases/tag/appkiro-password-manager-v1.0.17) |
| Update package signature | [.sig](https://github.com/ngankt2/appkiro.com/releases/download/appkiro-password-manager-v1.0.17/KiroPasswordManager_1.0.17_arm64.app.tar.gz.sig) |
| SHA-256 checksums | [SHA256SUMS](https://github.com/ngankt2/appkiro.com/releases/download/appkiro-password-manager-v1.0.17/SHA256SUMS) |
| Update channel | [latest.json](https://raw.githubusercontent.com/ngankt2/appkiro.com/main/updates/appkiro-password-manager/latest.json) |
| Release history | [All Kiro Password Manager releases](https://github.com/ngankt2/appkiro.com/releases?q=appkiro-password-manager) |

Learn more at [appkiro.com](https://appkiro.com).
