import os

def main():
    plan_text = "Day 1: find 300 Shopify stores with slow mobile checkout (BuiltWith + PageSpeed, free). Email each owner a free 1-page audit, offer the $49 fix list or $199 done-for-you. Deliver fixes in code, invoice by Stripe link. Target: 6x$49 + 1x$199 = $493 by day 30."
    if not (1 <= len(plan_text) <= 280) or not plan_text.strip():
        import sys
        print("error: plan text must be 1 to 280 characters and not only whitespace", file=sys.stderr)
        sys.exit(1)
    os.makedirs('/output', exist_ok=True)
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write(plan_text)

if __name__ == "__main__":
    main()
