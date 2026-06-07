# Manual Upload Checklist

Use this checklist after reviewing the product package. Do not automate these steps unless you have a separate, intentional publishing workflow.

## Gumroad

1. Log in to Gumroad.
2. Create a new product.
3. Choose digital product.
4. Upload `dist/bountylens-0.1.0.zip`.
5. Copy the product title, short description, long description, FAQ, and disclaimer from `gumroad-listing.md`.
6. Set prices:
   - Personal: $19
   - Pro: $49
   - Team: $149
7. Upload screenshots:
   - Extension panel
   - Extension popup
   - CLI report
   - Prompt pack
   - Landing page hero
8. Set or paste the refund policy from `refund-policy.md`.
9. Manually complete payout, tax, and KYC requirements inside Gumroad.
10. Preview the checkout page and publish when ready.

## Lemon Squeezy

1. Log in to Lemon Squeezy.
2. Create a product.
3. Upload `dist/bountylens-0.1.0.zip`.
4. Copy product description, onboarding email, changelog blurb, and refund note from `lemon-squeezy-listing.md`.
5. Set product variants:
   - Personal: $19
   - Pro: $49
   - Team: $149
6. Enable license keys only if you want to use license management for the Pro or Team version. BountyLens itself does not call a license server.
7. Manually complete payout, tax, and KYC requirements inside Lemon Squeezy.
8. Preview the product page and publish when ready.

## Before Publishing

- Replace `Your Name` in `LICENSE` if needed.
- Add real screenshots.
- Review privacy and refund policy language for your jurisdiction.
- Confirm the ZIP opens on a clean machine.
- Confirm no platform listing promises guaranteed bounty earnings.
- Keep payment, KYC, payout, and tax setup manual.
