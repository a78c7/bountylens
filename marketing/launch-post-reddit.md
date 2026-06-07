# Reddit Launch Post

## Suggested Title

I built a local GitHub bounty issue scanner for open source contributors

## Body

I built BountyLens, a small local-first toolkit for screening GitHub issues that mention bounties, rewards, or funded work.

The idea is not to promise money or automate bounty hunting. It is a preflight check before spending time on an issue or handing it to Codex / an AI coding agent.

What it includes:

- Chrome extension for GitHub issue pages.
- Python CLI with no third-party dependencies.
- Markdown and JSON reports.
- Prompt templates for candidate review, pilot analysis, draft PR attempt, and PR status check.
- Static landing page and sales copy templates.

It checks for:

- Bounty / reward / funded wording.
- Possible amounts like `$50` or `USD 100`.
- Known platform signals like IssueHunt, Algora, Bountysource, Gitcoin, and Opire.
- Fake or weak reward wording.
- Existing or likely competing PR signals.
- High-risk categories like security, auth, payment, crypto, KYC, and database migration.
- External environment requirements such as hardware, cloud accounts, or deployment access.

Safety boundaries:

- No tracking.
- No GitHub token.
- No cookie access.
- No external server.
- No automatic issue comments.
- No automatic bounty claiming.
- No automatic PR creation.
- No payment, KYC, payout, or withdrawal handling.

This does not guarantee bounty earnings. It is a lightweight local screening tool that helps avoid obvious bad candidates before deeper manual review.

Download: https://example.com/buy

Feedback welcome, especially from people who contribute to open source or use AI coding agents for issue triage.

## Subreddit Notes

- `r/SideProject`: emphasize the product build and local-first scope.
- `r/opensource`: emphasize manual review, no PR spam, no bounty claiming automation.
- `r/webdev`: emphasize Chrome extension, CLI, and developer workflow.
