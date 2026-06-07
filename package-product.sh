#!/usr/bin/env bash
set -euo pipefail

VERSION="0.1.0"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ZIP_PATH="$ROOT_DIR/dist/bountylens-$VERSION.zip"

cd "$ROOT_DIR"
mkdir -p dist
rm -f "$ZIP_PATH"

required_files=(
  "README.md"
  "QUICKSTART.md"
  "CHANGELOG.md"
  "LICENSE"
  "CONTRIBUTING.md"
  "SECURITY.md"
  "CODE_OF_CONDUCT.md"
  "OPEN_SOURCE_READY_REPORT.md"
  "GITHUB_OPEN_SOURCE_REPORT.md"
  ".gitignore"
  ".github/workflows/test.yml"
  ".github/ISSUE_TEMPLATE/bug_report.md"
  ".github/ISSUE_TEMPLATE/feature_request.md"
  ".github/ISSUE_TEMPLATE/safety_rule.md"
  ".github/PULL_REQUEST_TEMPLATE.md"
  "privacy-policy.md"
  "refund-policy.md"
  "gumroad-listing.md"
  "lemon-squeezy-listing.md"
  "extension/manifest.json"
  "extension/content.js"
  "extension/popup.html"
  "extension/popup.js"
  "extension/styles.css"
  "extension/icons/icon16.svg"
  "extension/icons/icon48.svg"
  "extension/icons/icon128.svg"
  "cli/bountylens.py"
  "cli/sample_config.json"
  "prompts/candidate-review.goal.md"
  "prompts/single-candidate-pilot.goal.md"
  "prompts/formal-draft-pr-attempt.goal.md"
  "prompts/pr-status-check.goal.md"
  "examples/sample-github-issue.html"
  "examples/sample-report.md"
  "examples/sample-candidate-list.md"
  "landing/index.html"
  "landing/styles.css"
  "marketing/manual-upload-checklist.md"
  "marketing/launch-post-x.md"
  "marketing/launch-post-linkedin.md"
  "marketing/launch-post-reddit.md"
  "marketing/product-hunt-copy.md"
  "marketing/email-announcement.md"
  "marketing/screenshot-plan.md"
  "marketing/demo-script.md"
  "marketing/faq-for-buyers.md"
  "marketing/pricing-strategy.md"
  "screenshots/README.md"
  "screenshots/png-placeholder-note.md"
  "screenshots/screenshot-01-extension-panel.html"
  "screenshots/screenshot-02-popup.html"
  "screenshots/screenshot-03-cli-report.html"
  "screenshots/screenshot-04-prompt-pack.html"
  "screenshots/screenshot-05-landing-page.html"
  "screenshots/screenshot-06-workflow.html"
  "tests/test_bountylens_cli.py"
)

for file in "${required_files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file" >&2
    exit 1
  fi
done

python3 -m unittest discover -s tests

zip -r "$ZIP_PATH" \
  README.md \
  QUICKSTART.md \
  CHANGELOG.md \
  LICENSE \
  CONTRIBUTING.md \
  SECURITY.md \
  CODE_OF_CONDUCT.md \
  OPEN_SOURCE_READY_REPORT.md \
  GITHUB_OPEN_SOURCE_REPORT.md \
  .gitignore \
  .github \
  privacy-policy.md \
  refund-policy.md \
  gumroad-listing.md \
  lemon-squeezy-listing.md \
  extension \
  cli \
  prompts \
  examples \
  landing \
  marketing \
  screenshots \
  tests \
  -x "*/.git/*" \
  -x "*/node_modules/*" \
  -x "*secrets*" \
  -x "*cookies*" \
  -x "*keychain*" \
  -x "*tokens*" \
  -x "*state.json" \
  -x "*codex-bounty-hunter*" \
  -x "*.DS_Store"

if unzip -l "$ZIP_PATH" | grep -Eiq '(^|/)(\.git|node_modules)(/|$)|secrets|cookies|keychain|tokens|state\.json|codex-bounty-hunter'; then
  echo "Sensitive or excluded path found in zip listing." >&2
  exit 1
fi

echo "Created $ZIP_PATH"
