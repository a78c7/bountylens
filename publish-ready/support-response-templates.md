# Support Response Templates

## 1. Download ZIP Issue

Hi,

Thanks for reaching out. Please try downloading `bountylens-0.1.0.zip` again from your receipt or customer portal.

After download, unzip the package and confirm these files exist:

- `README.md`
- `QUICKSTART.md`
- `extension/`
- `cli/`
- `prompts/`

If the ZIP still cannot be opened, send a screenshot of the error and your purchase email. I will help verify the download.

## 2. Chrome Extension Installation

Hi,

To install the BountyLens Chrome extension:

1. Open `chrome://extensions`.
2. Enable `Developer mode`.
3. Click `Load unpacked`.
4. Select the `extension/` folder inside the unzipped BountyLens package.
5. Open a GitHub issue URL matching `https://github.com/*/*/issues/*`.

BountyLens runs locally on visible issue page text and does not need a GitHub token.

## 3. CLI Cannot Run

Hi,

Please confirm Python 3 is installed:

```bash
python3 --version
```

Then run this from the BountyLens folder:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html
```

The CLI uses Python standard library only. If it still fails, send the command you ran, your operating system, and the terminal error output.

## 4. Guaranteed Earnings Question

Hi,

BountyLens does not guarantee bounty earnings. It is a screening workflow for identifying bounty signals, fake or weak reward wording, high-risk categories, and review suitability before you spend time on an issue.

Maintainers, bounty platforms, rules, timing, and competing contributors determine actual outcomes.

## 5. Automatic Bounty Claim Question

Hi,

BountyLens does not automatically claim bounties. It also does not comment on issues, create pull requests automatically, process KYC, handle payments, manage payouts, or perform withdrawals.

Any bounty claim or platform action must be handled manually by you on the relevant platform.

## 6. Refund Request

Hi,

Thanks for the note. BountyLens has a 7-day refund window for broken downloads, missing files, or a product that cannot be opened.

Please send:

- Purchase email.
- Purchase date.
- Short description of the issue.
- Screenshot or error output if relevant.

I will review the request against the refund policy.

## 7. Windows Path Issue

Hi,

On Windows, unzip BountyLens into a simple folder path, for example:

```text
C:\Users\YourName\Downloads\bountylens
```

Then open PowerShell in that folder and run:

```powershell
python cli\bountylens.py --html examples\sample-github-issue.html
```

If `python` does not work, try:

```powershell
py cli\bountylens.py --html examples\sample-github-issue.html
```

## 8. Team Version Question

Hi,

The first launch is the Personal version at $19. A Team/Internal version is planned as a future tier around $149 for small teams that want shared workflow docs and a team safety checklist.

For now, you can use the Personal package for individual use. If you need team usage, reply with your expected seat count and workflow so I can prioritize the right license terms.
