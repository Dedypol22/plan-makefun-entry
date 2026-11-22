import os

def main():
    plan_text = "Day 1: find 300 Shopify stores with slow mobile checkout (BuiltWith + PageSpeed, free). Email each owner a free 1-page audit, offer the $49 fix list or $199 done-for-you. Deliver fixes in code, invoice by Stripe link. Target: 6x$49 + 1x$199 = $493 by day 30."
    os.makedirs('/output', exist_ok=True)
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write(plan_text)

if __name__ == "__main__":
    main()
