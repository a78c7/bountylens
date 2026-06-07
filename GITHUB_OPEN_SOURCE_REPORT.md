# GitHub Open Source Report

## Timestamp

2026-06-07 17:13:14 CST

## 1. Repo URL

```text
https://github.com/a78c7/bountylens
```

Repository:

- Name: `a78c7/bountylens`
- Visibility: public
- Default branch: `main`
- Description: `Safety-first GitHub bounty triage toolkit for developers and AI coding agents`

Topics:

- `github`
- `bounty`
- `ai-agent`
- `codex`
- `chrome-extension`
- `cli`
- `open-source`
- `issue-triage`
- `developer-tools`

## 2. Release URL

```text
https://github.com/a78c7/bountylens/releases/tag/v0.1.0
```

Release:

- Tag: `v0.1.0`
- Title: `BountyLens v0.1.0`
- Draft: no
- Prerelease: no
- Existing release was detected; no duplicate release was created.

## 3. Commit Hash

Latest open-source setup commit on `main`:

```text
0e3dc5c15bd008b30275b65abc3aeb6a2a441b5d
```

Release tag commit:

```text
8524bef4ec5f7afba6f0b0dea57b62286df52d29
```

The existing `v0.1.0` tag was not moved.

## 4. Tag

```text
v0.1.0
```

## 5. Tests Result

Status: pass.

Command:

```bash
python3 -m unittest discover -s tests
```

Result:

```text
Ran 9 tests in 0.082s
OK
```

Packaging also reran the test suite:

```text
Ran 9 tests in 0.080s
OK
```

## 6. GitHub Actions Status

Status: pass.

Latest verified run:

```text
Run: 27088311390
Workflow: Test
Commit: 0e3dc5c15bd008b30275b65abc3aeb6a2a441b5d
Status: completed
Conclusion: success
URL: https://github.com/a78c7/bountylens/actions/runs/27088311390
```

## 7. Package Asset

Uploaded GitHub Release asset:

```text
bountylens-0.1.0.zip
```

Download URL:

```text
https://github.com/a78c7/bountylens/releases/download/v0.1.0/bountylens-0.1.0.zip
```

Asset metadata:

- Content type: `application/zip`
- Size: `956677`
- SHA-256 digest: `3158b20080aaac968788a8e3c5a633beafe2c7c8b9eafabc104410d10467ab16`
- State: `uploaded`

Local rebuilt package:

```text
dist/bountylens-0.1.0.zip
```

Because the release already existed, no duplicate release was created and the existing asset was left in place.

## 8. Security Scan Result

Status: pass.

Sensitive file-name scan:

```bash
find . \( -iname "*secret*" -o -iname "*token*" -o -iname "*.env*" -o -iname "*credential*" -o -iname "*cookie*" -o -iname "state.json" \) -print | sort
```

Result:

```text
no matching files
```

Release ZIP path scan passed for:

- `.git/`
- `node_modules`
- `.env`
- secrets
- cookies
- keychain
- tokens
- `state.json`
- `codex-bounty-hunter`

Extension permission review passed:

- `extension/manifest.json` is valid JSON.
- No `permissions` declaration.
- No `host_permissions` declaration.
- No `cookies` permission.
- No `webRequest` permission.
- No `tabs` permission.
- No broad host permissions.
- Content script limited to `https://github.com/*/*/issues/*`.

## 9. AgentGate Link

BountyLens helps before an AI agent starts work.

AgentGate helps after an AI agent creates a diff.

```text
https://github.com/a78c7/agentgate
```

## 10. Next Steps

Manual follow-up:

1. Open the GitHub repo page and confirm README rendering.
2. Download the release ZIP and confirm it opens.
3. Confirm local extension load instructions are clear.
4. Optionally link AgentGate and BountyLens in each repo README.
5. Optionally enable Discussions.
6. Optionally configure GitHub Pages for `landing/`.
7. Do not enable GitHub Sponsors unless the user later confirms a supported payout path and handles all payout/KYC/tax steps manually.

## Boundary Confirmation

- No `codex-bounty-hunter` project files were modified.
- AgentGate was not modified.
- No Gumroad login.
- No Lemon Squeezy login.
- No KYC, payment, payout, withdrawal, wallet, tax, or banking handling.
- No GitHub Sponsors setup.
- No paid product creation.
- No cookie, keychain, password manager, token, credential, `.env`, or `state.json` upload.
- No force push.
- No remote history overwrite.
