# Kiwi Password

[App catalog](../README.md) · [Appkiro website](https://appkiro.com) · [Product page](https://appkiro.com/kiwi-password-manager) · [Source code](https://github.com/ngankt2/kiwi-password-manager)

Kiwi Password (formerly Kiro Password Manager) is an offline, open-source password manager. It keeps passwords, two-factor codes, notes and files in an encrypted vault stored only on your device. No account, no cloud sync, no tracking.

## Features

- **Offline encrypted vault** — passwords, logins, secure notes, custom fields and attachments live in one encrypted file on your device. Nothing is uploaded.
- **Touch ID unlock** — the vault key is sealed by the Secure Enclave.
- **Built-in authenticator (TOTP)** — keep two-factor codes next to the login they protect.
- **KeePass import** — preview a `.kdbx` database and keep groups, custom fields, history, attachments, tags and OTP settings. The original file is never modified.
- **Version history and encrypted backups** — every entry keeps its previous versions; automatic and manual backups are encrypted.
- **Auto-lock and clipboard protection** — the vault locks when you leave it, and copied secrets are cleared automatically.

## Download and installation

| Detail | Current release |
| --- | --- |
| Version | **1.0.32** |
| Operating system | macOS 13 or later |
| Architecture | Separate builds for Apple Silicon and Intel |
| Signing | Apple Developer ID, notarized by Apple |
| License | GPL-3.0 |

- **[Download for Apple Silicon (M1, M2, M3, M4…)](https://github.com/ngankt2/kiwi-password-manager/releases/download/v1.0.32/KiwiPassword_1.0.32_apple-silicon.dmg)**
- **[Download for Intel Macs](https://github.com/ngankt2/kiwi-password-manager/releases/download/v1.0.32/KiwiPassword_1.0.32_intel.dmg)**

Not sure which one you need? Open Apple menu → **About This Mac**: a **Chip** line such as "Apple M1" means Apple Silicon; a **Processor** line with "Intel" means an Intel Mac.

1. Open the `.dmg`.
2. Drag **Kiwi Password** onto the **Applications** folder, following the arrow.
3. Open Kiwi Password from Applications.

## What's new in 1.0.32

- A new installer window: open the `.dmg` and drag Kiwi Password onto Applications. The installer volume carries the Kiwi Password icon.
- The app and installers remain signed with an Apple Developer ID and notarized by Apple.
- Kiwi Password is now open source under the GPL-3.0 license.

## Updates

Kiwi Password checks for updates at startup and every six hours while visible, and from Settings, the app menu or the version number in the footer. You choose when to download, install and restart. Every update is verified with the app's Minisign key before installation.

Versions 1.0.29 and later update themselves. Kiro Password Manager 1.0.28 and earlier used a different update channel and need one manual install of the latest `.dmg`.

| Update resource | Link |
| --- | --- |
| Current release | [Kiwi Password 1.0.32](https://github.com/ngankt2/kiwi-password-manager/releases/tag/v1.0.32) |
| Update channel | [latest.json](https://github.com/ngankt2/kiwi-password-manager/releases/latest/download/latest.json) |
| Release history | [All Kiwi Password releases](https://github.com/ngankt2/kiwi-password-manager/releases) |
| Earlier Kiro Password Manager releases | [Releases on appkiro.com](https://github.com/ngankt2/appkiro.com/releases?q=appkiro-password-manager) |

Learn more at [appkiro.com](https://appkiro.com/kiwi-password-manager).
