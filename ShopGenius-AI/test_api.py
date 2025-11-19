from api_handler import (
    parse_query,
    amazon_search,
    clean_results
)

print("🔥 Amazon Search Tester")
print("-------------------------")

while True:
    q = input("\nSearch: ")

    if q.lower() in ["exit", "quit", "close"]:
        print("Exiting tester...")
        break

    # 1️⃣ Parse User Query
    parsed = parse_query(q)
    print("\n🔍 Parsed Query Info:")
    print("   Brand:", parsed["brand"])
    print("   Price Limit:", parsed["price_limit"])
    print("   Keywords:", parsed["keywords"])

    # 2️⃣ Call Amazon API
    raw = amazon_search(parsed["keywords"])

    if not raw:
        print("\n❌ Error: No response from Amazon API\n")
        continue

    # 3️⃣ Clean & Filter Results
    products = clean_results(
        raw,
        brand=parsed["brand"],
        price_limit=parsed["price_limit"]
    )

    # 4️⃣ Display Final Results
    if not products:
        print("\n⚠ No matching products found.\n")
        continue

    print(f"\n✅ Found {len(products)} Matching Products:\n")

    for i, p in enumerate(products[:10], start=1):
        print(f"{i}. {p['title']}")
        print(f"   💰 Price: {p['price']}")
        print(f"   🔗 Link: {p['url']}")
        print()
