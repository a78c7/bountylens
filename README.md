# BountyLens

A safety-first GitHub bounty triage toolkit for developers and AI coding agents.

BountyLens 是一个安全优先的 GitHub bounty 候选筛选工具包，用来在让 Codex / AI agent 写 PR 之前，先判断 issue 是否值得做、是否有风险、是否像假 bounty。

## What Is BountyLens

BountyLens is an open-source toolkit for triaging public GitHub issue pages before a developer or AI coding agent starts implementation work.

It includes:

- A local Chrome extension for GitHub issue pages.
- A Python CLI for URL, HTML, or text input.
- A Codex-ready prompt pack for careful candidate review.
- Example reports, screenshots, and a static landing page.

BountyLens is not a bounty platform, payment tool, claim bot, or PR automation tool. It is a local decision aid before work starts.

## Why Bounty Issues Are Hard To Trust

GitHub issues that look like bounty opportunities can be ambiguous:

- The issue may mention rewards without a clear platform or payment path.
- Another contributor may already have a competing PR.
- The requested work may require private environments, credentials, production access, or maintainer-only context.
- The wording may look like a fake bounty or social engineering attempt.
- The work may involve auth, payment, tokens, crypto, KYC, or database migrations that should not be handled by an agent without explicit review.

BountyLens helps surface these signals before you ask Codex or another AI agent to write code.

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

## Screenshots

Screenshot assets live in `screenshots/`.

Recommended viewing order:

1. `screenshots/png/01-extension-panel.png`
2. `screenshots/png/03-cli-report.png`
3. `screenshots/png/06-workflow.png`
4. `screenshots/png/04-prompt-pack.png`
5. `screenshots/png/05-landing-page.png`
6. `screenshots/png/02-popup.png`

The HTML screenshot fixtures are also kept in `screenshots/` for repeatable local demo generation.

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

## Quickstart

Run the sample issue through the CLI:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

Build the release ZIP:

```bash
bash package-product.sh
```

## Example Workflow

```text
GitHub issue
-> BountyLens triage
-> Manual confirmation
-> Codex candidate review
-> Docker/testability check
-> Draft PR only after approval
-> Maintainer review
-> Manual platform rules and bounty claim
```

Typical local flow:

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

- Guarantee bounty earnings.
- Claim rewards.
- Handle KYC, payment, payout, withdrawal, wallet, tax, or banking flows.
- Read cookies.
- Read keychain data.
- Read GitHub tokens.
- Read passwords, private credentials, or password managers.
- Comment on issues.
- Create PRs automatically.
- Send issue text to a server.
- Track users or use telemetry.

Human confirmation is required before implementation, PR creation, bounty claiming, or any platform-specific process.

## What BountyLens Does Not Do

BountyLens does not make a final business, legal, or security decision. A `good_candidate_to_review` recommendation only means the issue looks worth human review under the current rules.

BountyLens does not replace:

- Maintainer confirmation.
- Bounty platform rules.
- Human code review.
- Security review.
- Payment, tax, or KYC processes.
- AgentGate or other post-diff safety checks.

## Relationship With AgentGate

BountyLens helps before an AI agent starts work.

AgentGate helps after an AI agent creates a diff.

Use them together like this:

```text
GitHub issue
-> BountyLens triage
-> AI agent work
-> AgentGate diff check
-> human review
-> PR
```

AgentGate is available at:

https://github.com/a78c7/agentgate

## Optional Launch Assets

This repository includes optional launch and packaging materials from the original product preparation pass:

- `marketing/`
- `publish-ready/`
- `gumroad-listing.md`
- `lemon-squeezy-listing.md`

They are not the main open-source path and do not create any paid product by themselves. Do not log in to Gumroad or Lemon Squeezy, create a paid product, or handle payout/KYC/tax flows unless you do that manually outside this project.

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
