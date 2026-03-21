"""
SESSION 04 - QUESTION 3: SHOPPING LIST MANAGER
===============================================

Topics Covered: Lists, append(), extend(), sum(), min(), max()

TASK:
Complete the four functions below to manage a shopping list.
All the printing and formatting is handled for you - just implement the logic!

DO NOT modify the test code at the bottom.
"""

def add_single_item(shopping_list, item):
    """
    Use append() to add a single item to the shopping list.

    Args:
        shopping_list: list of items
        item: string to add

    Returns:
        None (modifies the list in place)

    Example:
        lst = ["milk", "eggs"]
        add_single_item(lst, "bread")
        # lst is now ["milk", "eggs", "bread"]
    """
    shopping_list.append(item)
    # TODO: Use append() to add the item
    pass


def add_multiple_items(shopping_list, items):
    """
    Use extend() to add multiple items to the shopping list.

    Args:
        shopping_list: list of items
        items: list of strings to add

    Returns:
        None (modifies the list in place)

    Example:
        lst = ["milk"]
        add_multiple_items(lst, ["eggs", "bread", "butter"])
        # lst is now ["milk", "eggs", "bread", "butter"]
    """
    shopping_list.extend(items)
    # TODO: Use extend() to add all items
    pass


def calculate_total(prices):
    """
    Use sum() to calculate the total price.

    Args:
        prices: list of numbers (float or int)

    Returns:
        float - the sum of all prices

    Example:
        calculate_total([10.50, 5.25, 3.00]) should return 18.75
    """
    return sum(prices)
    # TODO: Use sum() to add up all prices
    pass


def find_price_range(prices):
    """
    Use min() and max() to find the cheapest and most expensive items.

    Args:
        prices: list of numbers (float or int)

    Returns:
        tuple: (min_price, max_price)

    Example:
        find_price_range([10.50, 5.25, 3.00]) should return (3.00, 10.50)
    """
    return (min(prices),max(prices))
    # TODO: Use min() and max() to find the range
    # Return them as a tuple: (min_price, max_price)
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def test_shopping_list():
    """Test function with formatted output"""
    print("=" * 60)
    print("SESSION 04 - QUESTION 3: SHOPPING LIST MANAGER")
    print("=" * 60)
    print()

    # Test 1: Add single item
    print("TEST 1: Add single item using append()")
    print("-" * 40)
    shopping_list = ["milk", "eggs"]
    print(f"Initial list: {shopping_list}")
    add_single_item(shopping_list, "bread")
    print(f"After adding 'bread': {shopping_list}")
    print(f"Expected: ['milk', 'eggs', 'bread']")
    print(f"Status: {'✓ PASS' if shopping_list == ['milk', 'eggs', 'bread'] else '✗ FAIL'}")
    print()

    # Test 2: Add multiple items
    print("TEST 2: Add multiple items using extend()")
    print("-" * 40)
    print(f"Current list: {shopping_list}")
    new_items = ["butter", "cheese", "yogurt"]
    print(f"Adding: {new_items}")
    add_multiple_items(shopping_list, new_items)
    print(f"After extend: {shopping_list}")
    expected = ['milk', 'eggs', 'bread', 'butter', 'cheese', 'yogurt']
    print(f"Expected: {expected}")
    print(f"Status: {'✓ PASS' if shopping_list == expected else '✗ FAIL'}")
    print()

    # Test 3: Calculate total
    print("TEST 3: Calculate total price using sum()")
    print("-" * 40)
    prices = [3.50, 2.25, 2.00, 4.75, 3.25, 1.50]
    print(f"Prices: {prices}")
    total = calculate_total(prices)
    print(f"Total: ${total:.2f}")
    print(f"Expected: $17.25")
    print(f"Status: {'✓ PASS' if abs(total - 17.25) < 0.01 else '✗ FAIL'}")
    print()

    # Test 4: Find price range
    print("TEST 4: Find price range using min() and max()")
    print("-" * 40)
    print(f"Prices: {prices}")
    min_price, max_price = find_price_range(prices)
    print(f"Cheapest item: ${min_price:.2f}")
    print(f"Most expensive item: ${max_price:.2f}")
    print(f"Expected: $1.50 and $4.75")
    print(f"Status: {'✓ PASS' if (min_price == 1.50 and max_price == 4.75) else '✗ FAIL'}")
    print()

    # Complete shopping summary
    print("=" * 60)
    print("SHOPPING SUMMARY")
    print("=" * 60)
    print(f"Items in cart: {len(shopping_list)}")
    for i, item in enumerate(shopping_list, start=1):
        print(f"  {i}. {item}")
    print()
    print(f"Total items: {len(shopping_list)}")
    print(f"Total cost: ${total:.2f}")
    print(f"Average price: ${total/len(prices):.2f}")
    print(f"Price range: ${min_price:.2f} - ${max_price:.2f}")
    print()
    print("=" * 60)


if __name__ == "__main__":
    test_shopping_list()
