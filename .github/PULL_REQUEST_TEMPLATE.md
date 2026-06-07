# Pull Request

## Summary

Describe the change.

## Changes

-

## Tests

Paste test commands and results.

```bash
python3 -m unittest discover -s tests
python3 cli/bountylens.py --html examples/sample-github-issue.html --output examples/generated-report.md
```

## Safety Impact

- Does this add telemetry?
- Does this read cookies/tokens/passwords?
- Does this read keychain data, password managers, or private credentials?
- Does this auto-comment or auto-create PR?
- Does this automatically claim rewards?
- Does this handle KYC/payment/withdrawal?
- Does this change Chrome extension permissions?
- Does this add external network access?

## Packaging

If packaging changed, run:

```bash
bash package-product.sh
```

## Notes

Keep PRs focused and avoid unrelated refactors.
