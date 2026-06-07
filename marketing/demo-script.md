# 3-Minute Demo Script

## 0:00-0:25 - Problem

"GitHub bounty issues can look attractive, but they are hard to judge quickly. Some are real, some are stale, some are already being worked on, and some point into risky areas like auth, payment, crypto, KYC, security, or database migration."

"Before spending time coding or asking an AI agent to help, I want a fast local preflight check."

## 0:25-0:50 - Open A GitHub Issue

"Here is a GitHub issue page that mentions a funded reward. I have installed BountyLens as an unpacked Chrome extension."

"BountyLens only reads visible issue page text. It does not read cookies, GitHub tokens, browser history, or account credentials."

## 0:50-1:25 - BountyLens Shows Risk

"The panel shows whether there is a bounty signal, whether an amount was found, which platform is mentioned, and whether risk flags were detected."

"In this example, it sees an IssueHunt-style funded signal and a $50 amount, with a recommendation to run a deeper candidate review."

"If the issue mentioned security, auth, payment, crypto, KYC, production database work, fake reward wording, or a likely competing PR, BountyLens would flag that instead."

## 1:25-1:50 - Copy Codex Review Prompt

"From the extension popup I can copy a short Codex review prompt."

"That prompt asks for a read-only candidate review. It explicitly says not to claim the bounty, not to comment, not to create a PR, and not to touch cookies, keychains, payment, KYC, or high-risk categories."

## 1:50-2:25 - Run The CLI

"There is also a Python CLI. It uses the standard library only."

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
```

"The CLI can analyze a public URL, local HTML file, or raw text, and it can output Markdown or JSON."

## 2:25-2:45 - Generated Report

"The generated report includes the URL, title, bounty signal, platform signal, possible amount, risk flags, forbidden flags, external environment flags, confidence, recommendation, and suggested next step."

"This becomes the handoff into manual confirmation or a Codex candidate review."

## 2:45-3:00 - Safety Boundary And CTA

"BountyLens does not guarantee bounty earnings. It does not claim bounties, process payments, handle KYC, or create pull requests automatically."

"It is a local screening toolkit for deciding whether an issue deserves deeper review before coding."

"Download the toolkit here: https://example.com/buy"
