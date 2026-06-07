# Post-Purchase Email

Subject: Your BountyLens download is ready

Hi,

Thank you for purchasing BountyLens.

## Download Instructions

1. Download `bountylens-0.1.0.zip` from your purchase receipt or customer portal.
2. Unzip the file.
3. Open `QUICKSTART.md`.

## Install The Chrome Extension

1. Open Chrome.
2. Go to `chrome://extensions`.
3. Enable `Developer mode`.
4. Click `Load unpacked`.
5. Select the `extension/` folder from the unzipped BountyLens package.
6. Open a GitHub issue page and review the BountyLens panel.

## Run The CLI

From the BountyLens folder:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html
```

Write a report:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
```

## Safety Note

BountyLens is a screening tool. It does not guarantee bounty earnings, claim rewards, create pull requests automatically, read cookies, read GitHub tokens, handle payment, process KYC, manage payouts, or perform withdrawals.

Always confirm bounty platform rules, maintainer expectations, payout status, and competing PRs manually.

## Support

If you need help, reply to this email or contact:

```text
support@example.com
```

## Refund Window

There is a 7-day refund window for broken downloads, missing files, or a product that cannot be opened. Refunds do not cover guaranteed earnings expectations, unsupported custom workflows, or misuse outside the stated safety boundaries.

Thanks,

Your Name
