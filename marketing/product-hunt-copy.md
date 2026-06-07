# Product Hunt Copy

## Tagline

Local GitHub bounty issue scanner for open source contributors

## Description

BountyLens is a local-first Chrome extension, Python CLI, and Codex prompt pack for screening GitHub issue pages that mention bounties, rewards, or funded work.

It checks visible issue text for bounty signals, possible amounts, known platform mentions, fake or weak reward wording, competing PR risk, external environment requirements, and high-risk task categories such as security, auth, payment, crypto, KYC, and database migration.

No tracking, no GitHub token, no cookies, no external server, no automatic bounty claiming, and no automatic PR creation.

## Maker Comment

I built BountyLens because bounty-style GitHub issues can look promising, but they are often hard to evaluate quickly.

Before coding, I want to know:

- Is there a real bounty signal?
- Is there an amount?
- Does a known platform appear?
- Is the reward wording weak or fake?
- Is someone already working on it?
- Is the task too risky for a Codex / AI-agent workflow?

BountyLens keeps that first pass local. The extension reads visible GitHub issue text, and the CLI can scan a public URL, local HTML file, or raw text. The included prompts help move from screening to a read-only candidate review before any implementation.

It does not guarantee bounty earnings and does not handle claims, payment, KYC, payout, or withdrawals.

## First Comment

Thanks for checking out BountyLens.

The first version is intentionally simple:

- Manifest V3 Chrome extension
- Python standard-library CLI
- Prompt templates for Codex
- Static landing page and sales copy
- Local-only analysis

I would like feedback on the rule categories, especially around fake bounty signals, competing PR detection, and what should be considered too risky for an AI-assisted contribution workflow.
