# Privacy Policy

Template effective date: June 7, 2026

BountyLens is designed as a local-first tool for screening public GitHub issue pages and user-provided issue text.

## Chrome Extension

The Chrome extension analyzes visible GitHub issue page text locally in the browser. It does not:

- Track users.
- Use an external server.
- Send issue text to the developer.
- Read cookies.
- Read GitHub tokens.
- Read browser history.
- Access account login state.
- Handle payment, payout, withdrawal, KYC, wallet, or crypto operations.
- Automatically comment, claim bounties, or create pull requests.

The extension runs only on matching GitHub issue URLs:

```text
https://github.com/*/*/issues/*
```

## CLI

The CLI only processes the input provided by the user:

- A public URL passed with `--url`.
- A local HTML file passed with `--html`.
- Raw text passed with `--text`.

The CLI does not read cookies, GitHub tokens, keychain, password manager entries, credentials, or local account state. It does not write external state.

## Data Storage

BountyLens does not include server-side storage, analytics, telemetry, tracking pixels, or external JavaScript.

## Payments And Accounts

BountyLens does not process payments, KYC, payout setup, withdrawals, bounty claims, or platform account login. Any purchase platform, tax, payout, or KYC workflow is handled separately by the product seller and the relevant sales platform.

## Template Notice

This is a practical privacy policy template for a digital product. Adapt it to your exact business, jurisdiction, and sales platform before publishing.
