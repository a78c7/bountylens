# Pull Request

## Summary

Describe the change.

## Tests

Paste test commands and results.

```bash
python3 -m unittest discover -s tests
```

## Safety Boundary Review

- Does this affect extension permissions?
- Does this add external network access?
- Does this read cookies, tokens, passwords, keychain data, or credentials?
- Does this automatically comment on issues or PRs?
- Does this automatically create PRs?
- Does this automatically claim rewards?
- Does this handle KYC, payment, payout, withdrawal, wallet, tax, or banking flows?

## Packaging

If packaging changed, run:

```bash
bash package-product.sh
```

## Notes

Keep PRs focused and avoid unrelated refactors.
