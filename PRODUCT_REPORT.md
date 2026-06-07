# BountyLens Product Report

## 1. Product Overview

BountyLens is a local-first digital product for GitHub open source contributors. It helps screen public GitHub issue pages for bounty signals, possible amounts, fake or weak reward wording, competing PR risk, high-risk task categories, and suitability for a read-only Codex or AI-agent review.

The product includes a Chrome extension, Python CLI, prompt pack, landing page, example files, sales copy, privacy policy template, refund policy template, tests, and a packaging script.

## 2. File Tree

```text
bountylens/
  README.md
  QUICKSTART.md
  CHANGELOG.md
  LICENSE
  PRODUCT_REPORT.md
  gumroad-listing.md
  lemon-squeezy-listing.md
  privacy-policy.md
  refund-policy.md
  package-product.sh
  extension/
    manifest.json
    content.js
    popup.html
    popup.js
    styles.css
    icons/
      icon16.svg
      icon48.svg
      icon128.svg
  cli/
    bountylens.py
    sample_config.json
  prompts/
    candidate-review.goal.md
    single-candidate-pilot.goal.md
    formal-draft-pr-attempt.goal.md
    pr-status-check.goal.md
  examples/
    sample-github-issue.html
    sample-report.md
    sample-candidate-list.md
    generated-report.md
  landing/
    index.html
    styles.css
  marketing/
    manual-upload-checklist.md
    launch-post-x.md
    launch-post-linkedin.md
    launch-post-reddit.md
    product-hunt-copy.md
    email-announcement.md
    screenshot-plan.md
    demo-script.md
    faq-for-buyers.md
    pricing-strategy.md
  screenshots/
    README.md
    screenshot-01-extension-panel.html
    screenshot-02-popup.html
    screenshot-03-cli-report.html
    screenshot-04-prompt-pack.html
    screenshot-05-landing-page.html
    screenshot-06-workflow.html
    png-placeholder-note.md
  tests/
    test_bountylens_cli.py
  dist/
    bountylens-0.1.0.zip
```

## 3. Implemented Features

- Manifest V3 Chrome extension scoped to `https://github.com/*/*/issues/*`.
- Extension panel that analyzes visible GitHub issue text locally.
- Extension popup with product description, safety principles, and a copyable Codex review prompt.
- Local JavaScript rule engine for bounty keywords, platform signals, amount extraction, fake signals, competing PR signals, forbidden categories, and external environment signals.
- Python CLI using standard library only.
- CLI inputs: `--url`, `--html`, and `--text`.
- CLI outputs: Markdown, JSON with `--json`, and file output with `--output`.
- CLI report fields: URL, title, bounty signal, platform signal, possible amounts, risk flags, forbidden flags, external environment flags, confidence, recommendation, and suggested next step.
- Prompt pack with explicit safety boundaries.
- Static landing page with no external JavaScript, no tracking, and placeholder sales links.
- Gumroad and Lemon Squeezy listing copy.
- Marketing launch pack with manual upload checklist, X, LinkedIn, Reddit, Product Hunt, email, screenshot, demo, and buyer FAQ materials.
- Local screenshot mock assets for extension, popup, CLI, prompt pack, landing page, and workflow sales images.
- Privacy and refund policy templates.

## 4. Test Results

Verified on June 7, 2026.

Command:

```bash
python3 -m unittest discover -s tests
```

Result:

```text
Ran 9 tests in 0.080s
OK
```

The packaging script also reran the test suite successfully before creating the ZIP.

## 5. Packaging Result

Verified on June 7, 2026.

Command:

```bash
bash package-product.sh
```

Created artifact:

```text
dist/bountylens-0.1.0.zip
```

ZIP contents were checked with `unzip -l`. The archive does not contain `.git`, `node_modules`, secrets, cookies, keychain paths, token paths, `state.json`, or `codex-bounty-hunter` reports.

Generated CLI example report:

```text
examples/generated-report.md
```

## 6. How To Sell

1. Review and customize the author name, policies, screenshots, and sales links.
2. Create a Gumroad or Lemon Squeezy product manually.
3. Upload `dist/bountylens-0.1.0.zip`.
4. Use the supplied listing copy as the starting sales description.
5. Set suggested prices:
   - Personal: $19
   - Pro: $49
   - Team: $149
6. Add real screenshots before publishing.

## 7. User Manual Next Steps

- Create a Gumroad or Lemon Squeezy product.
- Upload `dist/bountylens-0.1.0.zip`.
- Set product pricing.
- Manually handle KYC and payout setup in the sales platform.
- Manually publish and test the checkout flow.

## 8. Risk Boundaries

BountyLens does not log into platforms, read cookies, read keychain data, read password managers, access GitHub tokens, process payments, perform KYC, manage payouts, claim bounties, create comments, or create PRs.

The product should not be used for security, auth, token, secret, payment, billing, wallet, crypto, KYC, production database, or destructive migration tasks.

## 9. Future Version Suggestions

- Configurable keyword rules through a local JSON file.
- Browser panel export to Markdown.
- More platform-specific pattern detection.
- Better competing PR detection using visible linked PR elements.
- Optional local-only history with explicit user opt-in.
- Screenshot assets for the landing page and sales listings.

## Launch Readiness

- Ready for manual upload: yes
- Missing screenshots: no, HTML mock screenshots generated
- Suggested first price: $19
- Suggested launch bundle:
  - ZIP
  - Prompt pack
  - CLI
  - Extension
  - Landing page
- Recommended first channel:
  - Gumroad
  - Lemon Squeezy
  - X
  - Reddit SideProject

## Pricing Recommendation

- Recommended launch price: $19
- Why not free: the package is a complete workflow, not a loose script. A low paid price signals value while staying accessible.
- Why not high-ticket yet: v0.1.0 does not include hosted automation, platform integrations, support SLAs, testimonials, or guaranteed outcomes.
- When to raise price: after 5 to 10 real buyers, useful feedback, better screenshots, a demo video, and clearer Pro / Team demand.
- Suggested future tiers:
  - Personal: $19
  - Pro: $49
  - Team/Internal: $149

Start with one Personal product at $19 and label it as a launch price. Do not promise guaranteed bounty earnings, automatic bounty claims, or automatic PR success.

## Screenshot Assets

Generated HTML screenshot sources:

- `screenshots/screenshot-01-extension-panel.html`
- `screenshots/screenshot-02-popup.html`
- `screenshots/screenshot-03-cli-report.html`
- `screenshots/screenshot-04-prompt-pack.html`
- `screenshots/screenshot-05-landing-page.html`
- `screenshots/screenshot-06-workflow.html`

PNG output directory, if generated:

```text
screenshots/png/
```

Generated PNG screenshots:

- `screenshots/png/01-extension-panel.png`
- `screenshots/png/02-popup.png`
- `screenshots/png/03-cli-report.png`
- `screenshots/png/04-prompt-pack.png`
- `screenshots/png/05-landing-page.png`
- `screenshots/png/06-workflow.png`

If PNG generation is unavailable on a future machine, open the HTML files locally in a browser and capture screenshots manually.

## Manual Publishing Steps

1. Open Gumroad or Lemon Squeezy.
2. Create a digital product.
3. Set price to $19.
4. Upload `dist/bountylens-0.1.0.zip`.
5. Upload screenshots.
6. Paste listing copy.
7. Set refund policy.
8. Complete payout, KYC, and tax requirements yourself.
9. Publish.
