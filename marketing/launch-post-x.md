# X / Twitter Launch Posts

## Short Version

I built BountyLens: a local Chrome extension + Python CLI + Codex prompt pack for screening GitHub bounty issues before you spend time on them.

It checks bounty signals, possible amount, fake reward wording, competing PR risk, and high-risk categories.

No tracking. No GitHub token. No payout handling.

Download: https://example.com/buy

## Technical Version

New side project: BountyLens.

It is a local-first toolkit for GitHub bounty triage:

- Manifest V3 Chrome extension for GitHub issue pages
- Python CLI with standard library only
- Markdown / JSON reports
- Codex prompt pack for candidate review and draft PR workflow
- No cookies, no token, no external API, no tracking

It flags bounty/reward/funded signals, known platforms like IssueHunt/Algora/Gitcoin, possible amounts, fake-bounty wording, competing PR risk, external environment requirements, and categories I do not want an AI agent touching.

Download: https://example.com/buy

## Safety Boundary Version

Bounty issues can look attractive, but some are stale, fake, already claimed, or too risky for an AI-agent workflow.

BountyLens is my local preflight scanner for that:

- Reads visible GitHub issue text locally
- Does not read cookies or GitHub tokens
- Does not claim bounties
- Does not auto-comment
- Does not create PRs
- Flags security/auth/payment/crypto/KYC/database migration risk

It does not guarantee earnings. It helps you avoid bad candidates before coding.

Download: https://example.com/buy
