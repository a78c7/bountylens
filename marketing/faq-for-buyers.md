# FAQ For Buyers

## 1. Does BountyLens guarantee I will make money?

No. BountyLens does not guarantee bounty earnings, bounty eligibility, maintainer acceptance, merge status, review speed, payout, or revenue. It is a screening tool.

## 2. Does it automatically submit pull requests?

No. The extension and CLI do not create pull requests. The prompt pack includes a guarded draft PR workflow, but it requires explicit user confirmation and limits the workflow to at most one PR.

## 3. Does it read my GitHub token?

No. BountyLens does not need or read a GitHub token.

## 4. Does it read cookies?

No. The extension does not request cookie permission, and the CLI does not read browser cookies.

## 5. Which bounty platforms does it support?

It detects text signals for IssueHunt, Opire, Algora, Bountysource, Gitcoin, and unknown platform wording such as bounty, reward, funded, sponsor, and backer.

## 6. Why are some issues marked avoid?

Issues may be marked avoid when they include fake or weak bounty wording, failed reward wording, security, auth, payment, wallet, crypto, KYC, production database, or destructive migration signals.

## 7. Can I use it with Codex?

Yes. The prompt pack includes Codex-ready `/goal` templates for candidate review, pilot analysis, draft PR attempts, and PR status checks.

## 8. Can I use it with Claude Code?

Yes, you can adapt the same prompts for Claude Code or another coding agent. Keep the same safety boundaries.

## 9. Does it support Windows, Mac, and Linux?

The Python CLI should run on Windows, Mac, and Linux with Python 3. The Chrome extension can be loaded in Chromium-based browsers that support Manifest V3 unpacked extensions.

## 10. Do I need to publish it to the Chrome Web Store?

No. Buyers can load it locally as an unpacked extension. Chrome Web Store publishing is optional and would require a separate manual review and publishing process.

## 11. Does the CLI require a GitHub token?

No. It can fetch public issue pages with `urllib`, analyze local HTML files, or analyze raw text.

## 12. Does my data upload to a server?

No. BountyLens has no external server, tracking, analytics, telemetry, or external JavaScript.

## 13. How do refunds work?

The included refund policy template suggests a 7-day refund window for broken downloads, missing files, or a product that cannot be opened. Adapt the policy before publishing.

## 14. Is it suitable for teams?

Yes, as a lightweight shared workflow. Teams should adapt the prompts, safety rules, pricing tier, and internal review process to their own policies.

## 15. How do I get future updates?

That depends on the seller's Gumroad or Lemon Squeezy setup. A typical approach is to send product update emails and replace the downloadable ZIP with the new version.

## 16. Does it claim bounties automatically?

No. It never claims bounties. Platform claims, payout setup, and bounty rules must be handled manually by the user.

## 17. Does it handle KYC, payouts, withdrawals, wallet setup, or payment flows?

No. BountyLens does not handle KYC, payout, withdrawal, wallet, crypto, tax, or payment operations.

## 18. Can it detect every fake bounty?

No. It detects common weak signals, but users must manually confirm platform status, payout rules, maintainer expectations, and existing PRs.

## 19. Can I customize the keyword rules?

Yes. The JavaScript and Python rule lists are plain text lists in `extension/content.js` and `cli/bountylens.py`.

## 20. Can it scan private repositories?

No. It is designed for visible GitHub issue text and public URL or user-provided input. It does not bypass login or access controls.
