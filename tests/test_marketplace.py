"""Catalog checks with a simulated GitHub API; host upgrades remain separate."""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch


spec = importlib.util.spec_from_file_location("marketplace", Path(__file__).resolve().parents[1] / "scripts/validate-marketplace.py")
marketplace = importlib.util.module_from_spec(spec)
spec.loader.exec_module(marketplace)


class MarketplaceTests(unittest.TestCase):
    def catalog(self, version="0.4.0"):
        return {"name": "ahmadabdalla-plugins", "plugins": [{
            "name": "aasystem", "version": version,
            "source": {"source": "url", "url": "https://github.com/ahmadabdalla/aasystem.git", "ref": f"v{version}"},
        }]}

    def test_stale_pr_cannot_downgrade_catalog_before_network_calls(self):
        with patch.object(marketplace, "github") as github:
            with self.assertRaisesRegex(ValueError, "must not decrease"):
                marketplace.validate(self.catalog("0.9.0"), self.catalog("0.10.0"))
            github.assert_not_called()

    def test_entry_skill_tracks_release_rename(self):
        import base64
        import json

        for version, entry in (("0.7.1", "aapilot"), ("0.8.0", "pilot"), ("0.10.0", "pilot")):
            with self.subTest(version=version):
                manifest = base64.b64encode(json.dumps({"name": "aasystem", "version": version}).encode()).decode()
                responses = [{"object": {"type": "commit", "sha": "a" * 40}},
                             {"tag_name": f"v{version}", "draft": False},
                             {"content": manifest}, {"content": manifest}, {}]
                with patch.object(marketplace, "github", side_effect=responses) as github:
                    marketplace.validate(self.catalog(version))
                    self.assertEqual(github.call_args.args[0],
                                     f"repos/ahmadabdalla/aasystem/contents/skills/{entry}/SKILL.md?ref={'a' * 40}")

    def test_unpublished_release_and_version_drift_are_rejected(self):
        import base64
        import json

        for draft, version, message in ((True, "0.4.0", "not published"),
                                        (False, "0.3.0", "identity/version differs"),
                                        (False, "0.4.0", None)):
            with self.subTest(draft=draft, version=version):
                manifest = base64.b64encode(json.dumps({"name": "aasystem", "version": version}).encode()).decode()
                responses = [{"object": {"type": "commit", "sha": "a" * 40}},
                             {"tag_name": "v0.4.0", "draft": draft},
                             {"content": manifest}, {"content": manifest}, {}]
                with patch.object(marketplace, "github", side_effect=responses):
                    if message:
                        with self.assertRaisesRegex(ValueError, message):
                            marketplace.validate(self.catalog(), self.catalog("0.3.0"))
                    else:
                        marketplace.validate(self.catalog(), self.catalog("0.3.0"))


if __name__ == "__main__":
    unittest.main()
