AgentProfiles 1.0.34 packages the current desktop source for macOS on Apple Silicon and Intel.

Changes since the previous public build:

- Desktop and Terminal tabs sit below search for easier navigation.
- Account details remain available after closing profiles or restarting the app.
- Compact controls and clearer selected states improve the workspace and Light appearance.
- The wider profile editor keeps all color options together.

Download `AgentProfiles_1.0.34_universal-local.dmg`, open it, and drag AgentProfiles to Applications.

This build uses an ad hoc signature and is not notarized by Apple. macOS Gatekeeper may block it when downloaded. The updater package has a separate cryptographic signature; that signature does not replace Apple notarization.

Validation: 85 JavaScript tests, 131 Rust tests, 6 update-interface tests, and 3 packaging tests passed. Eight Rust tests requiring configured external apps or accounts were skipped. The universal executable, application signature, and mounted installer contents were verified.

Website: https://appkiro.com/agent-profiles
