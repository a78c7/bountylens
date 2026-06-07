/goal

Review one GitHub issue as a possible bounty candidate. This is a read-only candidate review.

Inputs:
- GitHub issue URL: paste here
- Optional bounty platform URL: paste here

Tasks:
1. Read only public issue and repository content.
2. Identify bounty or reward signals, possible amount, and platform.
3. Check whether the bounty may be fake, failed, placeholder, demo, or unrelated to this issue.
4. Check whether there is an existing competing PR or maintainer activity that changes the opportunity.
5. Check whether the work appears testable locally without special accounts or private systems.
6. Classify the issue as good_candidate_to_review, manual_confirmation_needed, avoid, or not_a_bounty.
7. Return a concise Markdown report with evidence links and a next-step recommendation.

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
