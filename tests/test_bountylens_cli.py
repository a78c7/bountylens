import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = ROOT / "cli" / "bountylens.py"
spec = importlib.util.spec_from_file_location("bountylens_cli", CLI_PATH)
bountylens = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = bountylens
spec.loader.exec_module(bountylens)


class BountyLensCliTest(unittest.TestCase):
    def analyze(self, text):
        return bountylens.analyze_issue_text(text)

    def test_detects_issuehunt_funded_text(self):
        result = self.analyze("This issue is funded on IssueHunt with a $50 reward.")
        self.assertTrue(result.bounty_signal)
        self.assertEqual(result.platform_signal, "IssueHunt")
        self.assertEqual(result.recommendation, "good_candidate_to_review")

    def test_extracts_dollar_amount(self):
        result = self.analyze("Submit a pull request to get $50 from the sponsor.")
        self.assertIn("$50", result.possible_amounts)

    def test_detects_fake_reward_failed(self):
        result = self.analyze("IssueHunt reward failed. Failed to create reward below minimum reward.")
        self.assertIn("fake_or_weak_bounty_signal", result.risk_flags)
        self.assertEqual(result.recommendation, "avoid")

    def test_detects_security_exploit_forbidden(self):
        result = self.analyze("Bounty: fix a security exploit and RCE vulnerability.")
        self.assertIn("security_vulnerability", result.forbidden_flags)
        self.assertEqual(result.recommendation, "avoid")

    def test_detects_payment_crypto_kyc(self):
        result = self.analyze("Reward $100 for payment wallet crypto KYC billing support.")
        self.assertIn("payment_wallet_crypto_kyc", result.forbidden_flags)
        self.assertEqual(result.recommendation, "avoid")

    def test_detects_external_environment(self):
        result = self.analyze("Funded bounty $75 requires a real device and cloud account.")
        self.assertIn("real_device_or_hardware", result.external_environment_flags)
        self.assertIn("deployment_or_cloud_account", result.external_environment_flags)
        self.assertEqual(result.recommendation, "manual_confirmation_needed")

    def test_outputs_json(self):
        completed = subprocess.run(
            [sys.executable, str(CLI_PATH), "--text", "IssueHunt funded $50", "--json"],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["bounty_signal"])
        self.assertEqual(payload["platform_signal"], "IssueHunt")

    def test_sample_html_can_be_analyzed(self):
        completed = subprocess.run(
            [sys.executable, str(CLI_PATH), "--html", str(ROOT / "examples" / "sample-github-issue.html"), "--json"],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["platform_signal"], "IssueHunt")
        self.assertIn("$50", payload["possible_amounts"])
        self.assertEqual(payload["recommendation"], "good_candidate_to_review")

    def test_not_a_bounty(self):
        result = self.analyze("Regular issue: update docs and fix typo.")
        self.assertFalse(result.bounty_signal)
        self.assertEqual(result.recommendation, "not_a_bounty")


if __name__ == "__main__":
    unittest.main()
