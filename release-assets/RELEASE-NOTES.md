AgentProfiles 1.0.24 brings the current desktop app to a downloadable macOS Universal release.

- Filter Desktop and Terminal profiles by provider, alongside search and sorting.
- Keep newly created profiles visible when a previous filter or search would hide them.
- Refine the search field, refresh controls and profile list layout.
- View release history and the installed version in About.
- Manage profile storage and open its folders from the app.

Download `AgentProfiles_1.0.24_universal-local.dmg` for macOS 11 or later. One installer supports both Apple Silicon and Intel. Open the DMG and drag AgentProfiles into Applications.

This is an early access build with an ad hoc signature. It is not notarized by Apple, so Gatekeeper may require approval in System Settings → Privacy & Security before opening it. The updater signature verifies the package and does not replace Apple notarization.

Windows and Linux installers are coming soon. No mobile installer is included.

Validation: 75 JavaScript tests and 131 Rust tests passed; 8 environment-dependent Rust tests were skipped. The universal executable, app signature and mounted DMG contents were verified.

Website: https://appkiro.com/agent-profiles
