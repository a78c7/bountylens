/goal

After explicit user confirmation, attempt one small draft pull request for a reviewed GitHub bounty candidate.

Inputs:
- GitHub issue URL: paste here
- Candidate review report: paste here
- Repository path or public clone URL: paste here
- User confirmation: paste here

Tasks:
1. Re-check the issue, bounty signal, platform, amount, and competing PR status before coding.
2. Abort if the task now involves security, auth, payment, crypto, KYC, database migration, private infrastructure, or untestable external services.
3. Implement the smallest reasonable change for the issue.
4. Run focused tests and document results.
5. Prepare a clear draft PR title and body.
6. Create at most one draft PR only if the user has explicitly confirmed that action.
7. Do not claim the bounty. Leave all platform and payout steps to the user.

Safety boundaries:
- Do not read cookie, keychain, password manager, private token, or credential data.
- Do not handle KYC, payment, payout, withdrawal, wallet, or crypto operations.
- Do not process security, auth, token, secret, credential, payment, crypto, KYC, or database migration tasks.
- Do not bypass login or access controls.
- Do not automatically comment on issues or pull requests.
- Do not automatically claim a bounty.
- Do not create more than 1 PR.
- Do not use dangerous full access.
- Do not use yolo mode.
