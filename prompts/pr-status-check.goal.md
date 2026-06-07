/goal

Read only the current status of one pull request related to a GitHub bounty candidate.

Inputs:
- Pull request URL: paste here
- Related issue URL: paste here
- Optional bounty platform URL: paste here

Tasks:
1. Read public PR status, checks, review comments, maintainer comments, and related issue state.
2. Summarize whether the PR is open, draft, merged, closed, requested changes, or waiting on review.
3. Identify any requested changes without making edits.
4. Check whether a competing PR or changed issue state affects the bounty opportunity.
5. Return a concise status report and recommended next action.

Safety boundaries:
- Do not read cookie, keychain, password manager, private token, or credential data.
- Do not handle KYC, payment, payout, withdrawal, wallet, or crypto operations.
- Do not process security, auth, token, secret, credential, payment, crypto, KYC, or database migration tasks.
- Do not bypass login or access controls.
- Do not automatically comment on issues or pull requests.
- Do not automatically claim a bounty.
- Do not create a PR.
- Do not create more than 1 PR in any later workflow.
- Do not use dangerous full access.
- Do not use yolo mode.
