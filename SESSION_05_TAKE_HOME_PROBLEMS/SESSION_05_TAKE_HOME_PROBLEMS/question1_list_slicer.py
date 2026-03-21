"""
SESSION 05 - QUESTION 1: LIST SLICER
=====================================

Topics Covered: List slicing, list methods, list copying

TASK:
Complete the four functions below to manipulate lists using slicing and methods.
All the printing and formatting is handled for you - just implement the logic!

DO NOT modify the test code at the bottom.
"""

def get_first_three(items):
    return items[:3]


def get_every_second(items):
   return items[::2]


def reverse_list(items):
  return items[::-1]


def safe_copy_and_modify(original, new_item):
   copy=original.copy()
   copy.append(new_item)

   return copy


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def test_list_slicer():
    """Test function with formatted output"""
    print("=" * 60)
    print("SESSION 05 - QUESTION 1: LIST SLICER")
    print("=" * 60)
    print()

    # Test data
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print(f"Original list: {numbers}")
    print()

    # Test 1: First three
    print("TEST 1: Get first 3 items")
    print("-" * 40)
    first_three = get_first_three(numbers)
    print(f"Result: {first_three}")
    print(f"Expected: [10, 20, 30]")
    print(f"Status: {'✓ PASS' if first_three == [10, 20, 30] else '✗ FAIL'}")
    print()

    # Test 2: Every second
    print("TEST 2: Get every second item")
    print("-" * 40)
    every_second = get_every_second(numbers)
    print(f"Result: {every_second}")
    print(f"Expected: [10, 30, 50, 70, 90]")
    print(f"Status: {'✓ PASS' if every_second == [10, 30, 50, 70, 90] else '✗ FAIL'}")
    print()

    # Test 3: Reverse
    print("TEST 3: Reverse the list")
    print("-" * 40)
    reversed_list = reverse_list(numbers)
    print(f"Result: {reversed_list}")
    print(f"Expected: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]")
    print(f"Status: {'✓ PASS' if reversed_list == [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] else '✗ FAIL'}")
    print()

    # Test 4: Safe copy and modify (CRITICAL TEST!)
    print("TEST 4: Copy and modify (original should NOT change!)")
    print("-" * 40)
    original = [1, 2, 3, 4, 5]
    print(f"Original before: {original}")
    modified = safe_copy_and_modify(original, 999)
    print(f"Modified copy: {modified}")
    print(f"Original after: {original}")
    print()
    print(f"Modified copy correct? {'✓ PASS' if modified == [1, 2, 3, 4, 5, 999] else '✗ FAIL'}")
    print(f"Original unchanged? {'✓ PASS' if original == [1, 2, 3, 4, 5] else '✗ FAIL (YOU MODIFIED THE ORIGINAL!)'}")
    print()

    # Bonus tests
    print("=" * 60)
    print("BONUS TESTS: More slicing examples")
    print("=" * 60)
    print(f"Last 3 items: {numbers[-3:]}")
    print(f"Middle items (exclude first & last): {numbers[1:-1]}")
    print(f"Every third item: {numbers[::3]}")
    print()
    print("=" * 60)


if __name__ == "__main__":
    test_list_slicer()
