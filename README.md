# BountyLens

A safety-first GitHub bounty triage toolkit for developers and AI coding agents.

BountyLens 是一个安全优先的 GitHub bounty 候选筛选工具包，用来在让 Codex / AI agent 写 PR 之前，先判断这个 issue 是否值得做、是否有风险、是否像假 bounty。

This project is open source.

BountyLens:

- Does not guarantee bounty earnings.
- Does not claim rewards.
- Does not handle KYC, payment, payout, withdrawal, wallet, tax, or banking flows.
- Does not read cookies, keychain, GitHub tokens, passwords, private credentials, or password managers.
- Does not auto-comment on issues or pull requests.
- Does not auto-create pull requests.
- Does not send issue text to a server.

## Features

- Local GitHub issue page triage.
- Bounty, reward, funded, sponsor, and platform keyword detection.
- Possible amount extraction such as `$50`, `USD 100`, `USDC`, `DAI`, or `ICP`.
- Fake or weak bounty wording detection.
- Competing PR and external environment risk flags.
- High-risk category flags for security, auth, token, secret, payment, crypto, KYC, and database migration work.
- Markdown and JSON CLI reports.
- Codex prompt pack for read-only candidate review and careful follow-up workflows.

## Chrome Extension

The Chrome extension runs as a Manifest V3 content script on:

```text
https://github.com/*/*/issues/*
```

It analyzes visible page text locally and renders a BountyLens panel with:

- Bounty signal.
- Possible amount.
- Platform signal.
- Risk flags.
- Recommendation.

The extension does not request `cookies`, `webRequest`, `tabs`, broad host permissions, or GitHub token access.

## CLI

The CLI uses Python standard library only.

```bash
python3 cli/bountylens.py --url https://github.com/owner/repo/issues/123
python3 cli/bountylens.py --html examples/sample-github-issue.html
python3 cli/bountylens.py --text "IssueHunt funded $50 reward"
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
python3 cli/bountylens.py --text "IssueHunt funded $50 reward" --json
```

Report fields include:

- `url`
- `title`
- `bounty_signal`
- `platform_signal`
- `possible_amounts`
- `risk_flags`
- `forbidden_flags`
- `external_environment_flags`
- `confidence`
- `recommendation`
- `suggested_next_step`

Recommendation values:

- `good_candidate_to_review`
- `manual_confirmation_needed`
- `avoid`
- `not_a_bounty`

## Prompt Pack

The `prompts/` directory contains Codex-ready `/goal` templates:

- `candidate-review.goal.md`
- `single-candidate-pilot.goal.md`
- `formal-draft-pr-attempt.goal.md`
- `pr-status-check.goal.md`

Each prompt includes safety boundaries against credential access, KYC/payment/withdrawal handling, automatic bounty claims, automatic comments, and broad PR automation.

## Installation

Clone the repository:

```bash
git clone https://github.com/a78c7/bountylens.git
cd bountylens
```

Install the Chrome extension locally:

1. Open `chrome://extensions`.
2. Turn on `Developer mode`.
3. Click `Load unpacked`.
4. Select the `extension/` folder.
5. Open a public GitHub issue page.

Run the CLI with Python 3:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html
```

No third-party Python dependencies are required.

## Usage

Typical local workflow:

1. Open a GitHub issue page.
2. Read the BountyLens browser panel.
3. Confirm platform status, bounty terms, and competing PRs manually.
4. Run a read-only Codex candidate review using the prompt pack.
5. Check local testability before implementation.
6. Create at most one draft PR only after explicit human approval.
7. Let maintainers review and handle any bounty platform process manually.

## Safety Model

BountyLens is designed to keep triage local, explicit, and low-risk.

It does not:

- Track users.
- Use telemetry.
- Call an external analysis server.
- Read cookies.
- Read GitHub tokens.
- Read keychain, password manager, or credentials.
- Handle KYC, payment, payout, withdrawal, wallet, or tax flows.
- Automatically claim bounties.
- Automatically comment on issues or PRs.
- Automatically create PRs.
- Recommend work on security, auth, payment, crypto, KYC, or destructive database migration issues.

## Example Workflow

```text
GitHub issue
-> BountyLens triage
-> Manual confirmation
-> Codex candidate review
-> Docker/testability check
-> Draft PR
-> Maintainer review
-> Manual platform rules and bounty claim
```

## Development

Project layout:

```text
extension/      Chrome extension
cli/            Python CLI
prompts/        Codex prompt templates
examples/       Sample issue and reports
landing/        Static landing page
tests/          Python unittest suite
screenshots/    Local demo screenshot assets
marketing/      Optional launch copy
publish-ready/  Optional manual publishing helper docs
```

Do not add telemetry, credential access, cookie access, automatic bounty claiming, or KYC/payment/payout flows.

## Tests

Run:

```bash
python3 -m unittest discover -s tests
```

Generate the sample report:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
```

Build the release ZIP:

```bash
bash package-product.sh
```

## Release

Current release:

```text
v0.1.0
```

The packaged ZIP is generated at:

```text
dist/bountylens-0.1.0.zip
```

The ZIP is intended as a GitHub Release asset, not as a required committed binary.

## Contributing

Contributions are welcome if they preserve the safety model.

Before large changes, open an issue describing:

- What problem is being solved.
- Whether the change affects security boundaries.
- Whether it adds network access.
- Whether it reads cookies, tokens, passwords, or local credentials.
- Whether it changes PR, comment, claim, KYC, payment, or payout behavior.

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).
