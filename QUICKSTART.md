# BountyLens Quickstart

Use this guide to try BountyLens in about 5 minutes.

## 1. Install The Extension

1. Open Chrome.
2. Go to `chrome://extensions`.
3. Enable `Developer mode`.
4. Click `Load unpacked`.
5. Select the `extension/` folder inside this product package.

## 2. Open A GitHub Issue

Open a public issue page:

```text
https://github.com/owner/repo/issues/123
```

If the URL matches `https://github.com/*/*/issues/*`, BountyLens inserts a small local scan panel.

## 3. Review The Panel

Check:

- Bounty signal
- Possible amount
- Platform signal
- Risk flags
- Recommendation

Treat the panel as an initial screen only. Confirm platform status and issue context manually.

## 4. Copy A Codex Review Prompt

Open the BountyLens extension popup and click `Copy Codex review prompt`.

Use the prompt to ask Codex for a read-only candidate review. Do not start implementation until the candidate is confirmed.

## 5. Run The CLI

From the product folder:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html
```

Scan raw text:

```bash
python3 cli/bountylens.py --text "IssueHunt funded $50 reward for a Markdown formatting fix"
```

Write a report:

```bash
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
```

## 6. Read The Report

Open the generated Markdown report and review:

- `recommendation`
- `risk_flags`
- `forbidden_flags`
- `external_environment_flags`
- `suggested_next_step`

Good next step: run a read-only Codex candidate review before coding.
