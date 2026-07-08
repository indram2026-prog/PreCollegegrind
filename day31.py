"""
Grocery Analytics Tool
A self-contained script demonstrating zip, map, filter, and list comprehensions.
"""

def main():
    # 1. OUR INDEPENDENT DATA SETS
    items = ["Milk", "Eggs", "Apples", "Protein Powder", "Chocolate"]
    prices = [3.50, 4.00, 6.00, 45.00, 2.50]

    print("=== 🛒 GROCERY DATA TOOL ===\n")

    # -------------------------------------------------------------------------
    # 1. ZIP(): Combines parallel lists into pairs
    # -------------------------------------------------------------------------
    # Pairs each item string with its float price
    grocery_pairs = list(zip(items, prices))
    
    print("1. Paired Data (using zip):")
    print(f"   {grocery_pairs}\n")


    # -------------------------------------------------------------------------
    # 2. MAP(): Transforms every element in a list uniformly
    # -------------------------------------------------------------------------
    # Applies a 10% tax/inflation increase to every price in the list
    taxed_prices = list(map(lambda price: round(price * 1.10, 2), prices))
    
    print("2. Prices After 10% Tax (using map):")
    print(f"   Original: {prices}")
    print(f"   Taxed:    {taxed_prices}\n")


    # -------------------------------------------------------------------------
    # 3. FILTER(): Extracts elements that meet a true/false condition
    # -------------------------------------------------------------------------
    # Filters out only the items from our pairs where the price is under $5.00
    cheap_items = list(filter(lambda pair: pair[1] < 5.00, grocery_pairs))
    
    print("3. Cheap Items Under $5.00 (using filter):")
    for name, price in cheap_items:
        print(f"   - {name}: ${price:.2f}")
    print()


    # -------------------------------------------------------------------------
    # 4. LIST COMPREHENSION: Concise syntax for creating new lists
    # -------------------------------------------------------------------------
    # Loops through our pairs to pull out just the names of items under $10.00
    budget_friendly_names = [name for name, price in grocery_pairs if price < 10.00]
    
    print("4. Budget-Friendly Names (using List Comprehension):")
    print(f"   {budget_friendly_names}\n")

    print("============================")

if __name__ == "__main__":
    main()