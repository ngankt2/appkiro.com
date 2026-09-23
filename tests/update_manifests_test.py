import base64
import copy
import importlib.util
from pathlib import Path
import unittest

spec = importlib.util.spec_from_file_location("validation", Path(__file__).parents[1] / "scripts/validate-updates.py")
validation = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validation)


def manifest():
    # Format-only fixture. Real payloads are cryptographically verified by the app.
    signature = base64.b64encode(("untrusted comment: fixture\n" +
        base64.b64encode(b"ED" + bytes(72)).decode() + "\ntrusted comment: fixture\n" +
        base64.b64encode(bytes(64)).decode() + "\n").encode()).decode()
    return {"version": "1.2.3", "notes": "Test release", "pub_date": "2026-09-23T00:00:00Z", "platforms": {
        "darwin-aarch64": {"url": "https://github.com/ngankt2/appkiro.com/releases/download/agentprofiles-v1.2.3/AgentProfiles_1.2.3.app.tar.gz", "signature": signature},
    }}


class ManifestTests(unittest.TestCase):
    def test_bootstrap_is_empty_and_not_a_release(self):
        data = {"version": "0.0.0", "platforms": {}}
        self.assertEqual(validation.validate_manifest("agentprofiles", data), [])
        with self.assertRaises(ValueError):
            validation.validate_manifest("agentprofiles", data, allow_empty=False)
        data["version"] = "1.0.0"
        with self.assertRaises(ValueError):
            validation.validate_manifest("agentprofiles", data)

    def test_universal_payload_can_serve_two_architectures(self):
        data = manifest()
        data["platforms"]["darwin-x86_64"] = copy.deepcopy(data["platforms"]["darwin-aarch64"])
        self.assertEqual(len(validation.validate_manifest("agentprofiles", data)), 1)

    def test_other_apps_and_repo_wide_latest_cannot_enter_this_channel(self):
        for url in [
            "https://github.com/ngankt2/appkiro.com/releases/latest/download/latest.json",
            "https://github.com/ngankt2/appkiro.com/releases/download/otherapp-v1.2.3/App.app.tar.gz",
            "https://github.com/ngankt2/appkiro.com/releases/download/agentprofiles-v1.2.2/App.app.tar.gz",
            "https://github.com/other/repo/releases/download/agentprofiles-v1.2.3/App.app.tar.gz",
            "http://github.com/ngankt2/appkiro.com/releases/download/agentprofiles-v1.2.3/App.app.tar.gz",
        ]:
            data = manifest(); data["platforms"]["darwin-aarch64"]["url"] = url
            with self.subTest(url=url), self.assertRaises(ValueError):
                validation.validate_manifest("agentprofiles", data)

    def test_signatures_must_be_contents_and_have_valid_packet_lengths(self):
        for signature in ["App.app.tar.gz.sig", "", None, base64.b64encode(b"not a signature").decode()]:
            data = manifest(); data["platforms"]["darwin-aarch64"]["signature"] = signature
            with self.subTest(signature=signature), self.assertRaises(ValueError):
                validation.validate_manifest("agentprofiles", data)

    def test_macos_dmg_is_not_an_updater_payload(self):
        data = manifest(); entry = data["platforms"]["darwin-aarch64"]
        entry["url"] = entry["url"].replace(".app.tar.gz", ".dmg")
        with self.assertRaises(ValueError):
            validation.validate_manifest("agentprofiles", data)

    def test_invalid_versions_and_slugs(self):
        for version in ["1.02.3", "1.2.3-beta", "v1.2.3", "1.2", "", 1]:
            with self.subTest(version=version), self.assertRaises(ValueError):
                validation.version_tuple(version)
        for app in ["../other", "Other", "app/name"]:
            with self.assertRaises(ValueError):
                validation.validate_manifest(app, manifest())

    def test_windows_installer_type_must_match_target(self):
        data = manifest(); entry = data["platforms"].pop("darwin-aarch64")
        entry["url"] = entry["url"].replace(".app.tar.gz", ".msi")
        data["platforms"]["windows-x86_64-nsis"] = entry
        with self.assertRaises(ValueError):
            validation.validate_manifest("agentprofiles", data)


if __name__ == "__main__":
    unittest.main()
