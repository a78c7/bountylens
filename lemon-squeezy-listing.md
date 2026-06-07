# Lemon Squeezy Listing

## Product Name

BountyLens - GitHub Bounty Issue Scanner

## Product Description

BountyLens is a local-first toolkit for screening GitHub bounty issues before you spend time on them.

It includes a Chrome extension for GitHub issue pages, a Python CLI, Codex prompt templates, sample reports, a static landing page, and policy templates. It helps identify bounty signals, possible amounts, fake or weak reward wording, competing PR risk, and high-risk task categories such as security, auth, payment, crypto, KYC, and database migration.

No GitHub token. No cookies. No tracking. No hosted server. No payout handling.

Recommended launch variant: BountyLens Personal - $19.

This toolkit does not guarantee bounty earnings.

## Variant Ideas

- Personal - $19
  - Single user download.
  - Extension, CLI, prompts, examples.
- Pro - $49
  - Personal use plus editable sales and landing page templates.
  - Suggested for freelancers and indie hackers.
- Team - $149
  - Internal team use.
  - Suggested for small contributor teams using Codex or AI agents.

## Recommended Launch Variant

Start with:

```text
BountyLens Personal - $19
```

Future variants:

- Pro - $49
- Team - $149

License keys are not required for the first ZIP-only launch. If license keys are enabled, use them for a later version or for Pro / Team customer management.

## License Key Note

License keys are optional. BountyLens is a downloadable ZIP package and does not include built-in license activation. It can be sold without license keys. If Lemon Squeezy license keys are enabled, use them for download/customer management only. The product itself does not call a license server.

## Download Instructions

After purchase:

1. Download `bountylens-0.1.0.zip`.
2. Unzip the package.
3. Read `QUICKSTART.md`.
4. Install the Chrome extension from the `extension/` folder.
5. Run the CLI from the product directory:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html
```

## Customer Onboarding Email

Subject: Your BountyLens download is ready

Thanks for purchasing BountyLens.

Start here:

1. Download and unzip `bountylens-0.1.0.zip`.
2. Open `QUICKSTART.md`.
3. Install the Chrome extension with `chrome://extensions` -> `Developer mode` -> `Load unpacked`.
4. Run the sample CLI scan:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html
```

Important: BountyLens is a screening tool. It does not guarantee bounty earnings and does not handle payments, KYC, payouts, withdrawals, wallet operations, or bounty claims.

## Changelog Blurb

Version 0.1.0 includes the initial Chrome extension, Python CLI, Codex prompt pack, sample reports, landing page, sales copy, privacy policy template, refund policy template, tests, and packaging script.

## Refund Note

7-day refund window for broken downloads, missing files, or a product that cannot be opened. No refund for guaranteed bounty expectations, unsupported custom workflows, or use outside the stated safety boundaries.
