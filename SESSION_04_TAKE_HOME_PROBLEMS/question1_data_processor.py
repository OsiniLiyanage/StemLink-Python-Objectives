"""
SESSION 04 - QUESTION 1: DATA PROCESSOR
========================================

Topics Covered: map(), filter(), lambda functions

TASK:
Complete the three functions below to process a list of numbers.
All the printing and formatting is handled for you - just implement the logic!

DO NOT modify the test code at the bottom.
"""

def square_all(numbers):
    """
    Use map() and a lambda to square all numbers.

    Args:
        numbers: list of integers

    Returns:
        list of squared numbers

    Example:
        square_all([1, 2, 3, 4]) should return [1, 4, 9, 16]
    """
    return list(map(lambda num: num** 2, numbers))
    

    # TODO: Implement using map() and lambda
    pass
    

def filter_even(numbers):
    """
    Use filter() and a lambda to keep only even numbers.

    Args:
        numbers: list of integers

    Returns:
        list containing only even numbers

    Example:
        filter_even([1, 2, 3, 4, 5, 6]) should return [2, 4, 6]
    """
    return list(filter(lambda num:num%2==0, numbers))

    # TODO: Implement using filter() and lambda
    pass


def sum_above_threshold(numbers, threshold):
    """
    Use filter() with lambda to get numbers above threshold,
    then use sum() to add them up.

    Args:
        numbers: list of integers
        threshold: minimum value (exclusive)

    Returns:
        integer - sum of all numbers above threshold

    Example:
        sum_above_threshold([5, 10, 15, 20], 10) should return 35 (15 + 20)
    """
    return sum(filter(lambda num:num>threshold,numbers))
    # TODO: Implement using filter(), lambda, and sum()
    pass


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def test_data_processor():
    """Test function with formatted output"""
    print("=" * 60)
    print("SESSION 04 - QUESTION 1: DATA PROCESSOR")
    print("=" * 60)

    # Test data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(f"\nOriginal numbers: {numbers}")
    print()

    # Test 1: Square all numbers
    print("TEST 1: Square all numbers")
    print("-" * 40)
    squared = square_all(numbers)
    print(f"Result: {squared}")
    print(f"Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]")
    print(f"Status: {'✓ PASS' if squared == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] else '✗ FAIL'}")
    print()

    # Test 2: Filter even numbers
    print("TEST 2: Filter even numbers")
    print("-" * 40)
    evens = filter_even(numbers)
    print(f"Result: {evens}")
    print(f"Expected: [2, 4, 6, 8, 10]")
    print(f"Status: {'✓ PASS' if evens == [2, 4, 6, 8, 10] else '✗ FAIL'}")
    print()

    # Test 3: Sum above threshold
    print("TEST 3: Sum numbers above threshold (5)")
    print("-" * 40)
    result = sum_above_threshold(numbers, 5)
    print(f"Numbers above 5: {list(filter(lambda x: x > 5, numbers))}")
    print(f"Result: {result}")
    print(f"Expected: 40")
    print(f"Status: {'✓ PASS' if result == 40 else '✗ FAIL'}")
    print()

    # Bonus test with different data
    print("=" * 60)
    print("BONUS TEST: Different dataset")
    print("=" * 60)
    test_data = [15, 23, 8, 42, 16, 4, 30]
    print(f"Numbers: {test_data}")
    print(f"Squared: {square_all(test_data)}")
    print(f"Evens only: {filter_even(test_data)}")
    print(f"Sum above 20: {sum_above_threshold(test_data, 20)}")
    print()
    print("=" * 60)


if __name__ == "__main__":
    test_data_processor()
