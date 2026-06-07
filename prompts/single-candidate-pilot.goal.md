/goal

Prepare and analyze one GitHub bounty candidate without creating a pull request.

Inputs:
- GitHub issue URL: paste here
- Optional bounty platform URL: paste here
- Local workspace path: paste here

Tasks:
1. Read public issue, repository, README, contributing guide, and test instructions.
2. Confirm bounty signal, amount, platform, and obvious fake-bounty risks.
3. Check for existing competing PRs or maintainer comments that make work wasteful.
4. Inspect the repository locally if available, or clone only public source if the user approves.
5. Determine whether the change is small, testable, and suitable for Codex or an AI agent.
6. Produce a pilot plan with files likely to change, tests to run, and estimated risk.
7. Stop before implementation unless the user explicitly approves.

Safety boundaries:
- Do not read cookie, keychain, password manager, private token, or credential data.
- Do not handle KYC, payment, payout, withdrawal, wallet, or crypto operations.
- Do not process security, auth, token, secret, credential, payment, crypto, KYC, or database migration tasks.
- Do not bypass login or access controls.
- Do not automatically comment on issues or pull requests.
- Do not automatically claim a bounty.
- Do not create a PR in this pilot.
- Do not create more than 1 PR in any later workflow.
- Do not use dangerous full access.
- Do not use yolo mode.
