# Contributing

Thanks for helping improve BountyLens.

This project is safety-first. Contributions must preserve the local-only, no-credentials, no-payment, no-claiming model.

## Run Tests

```bash
python3 -m unittest discover -s tests
```

Generate the sample CLI report:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
```

Build the release ZIP:

```bash
bash package-product.sh
```

## Test The Extension Locally

1. Open `chrome://extensions`.
2. Enable `Developer mode`.
3. Click `Load unpacked`.
4. Select the `extension/` folder.
5. Open a public GitHub issue URL matching `https://github.com/*/*/issues/*`.
6. Confirm the BountyLens panel appears and only reads visible page text.

## Safety Rules

Do not add:

- Telemetry.
- Tracking.
- Cookie access.
- GitHub token access.
- Keychain or password manager access.
- Credential collection.
- Automatic bounty claiming.
- Automatic issue comments.
- Automatic PR creation.
- Payment, payout, withdrawal, wallet, tax, or KYC flows.
- Security exploit instructions.

## Before Large Changes

Open an issue before large changes, especially when a change:

- Adds network access.
- Changes extension permissions.
- Changes recommendation logic.
- Changes prompt safety boundaries.
- Touches packaging or release artifacts.

## Pull Request Checklist

Before opening a PR:

- Run the test suite.
- Confirm no sensitive files are added.
- Confirm extension permissions remain minimal.
- Explain whether safety boundaries changed.
- Keep the change focused.
