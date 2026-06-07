# Security Policy

BountyLens is designed as a local-first GitHub issue triage toolkit.

## Security Model

The Chrome extension analyzes visible GitHub issue text locally.

The CLI only processes the URL, HTML, or text that the user explicitly provides.

BountyLens does not:

- Use telemetry.
- Send issue text to an external server.
- Read cookies.
- Read GitHub tokens.
- Read keychain data.
- Read password manager data.
- Read private credentials.
- Handle KYC, payment, payout, withdrawal, wallet, tax, or banking flows.
- Automatically claim bounties.
- Automatically comment on issues or pull requests.
- Automatically create pull requests.

There is no auto bounty claiming path.

## Reporting Security Issues

Report vulnerabilities through GitHub issues or GitHub security advisories if available.

Please include:

- A clear description.
- Steps to reproduce.
- Expected behavior.
- Actual behavior.
- Whether extension permissions or local credential access are involved.

## Out Of Scope

Do not file bounty exploit instructions, weaponized payloads, credential theft examples, payment abuse flows, or KYC bypass instructions.

Reports should focus on keeping BountyLens safe, local, and explicit.
