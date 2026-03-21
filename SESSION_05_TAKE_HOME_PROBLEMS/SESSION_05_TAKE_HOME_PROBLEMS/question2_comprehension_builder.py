"""
SESSION 05 - QUESTION 2: COMPREHENSION BUILDER
===============================================

Topics Covered: List comprehensions with filtering

TASK:
Complete the four functions below using LIST COMPREHENSIONS.
All the printing and formatting is handled for you - just implement the logic!

IMPORTANT: Each function must be written as a SINGLE LINE using list comprehension!

DO NOT modify the test code at the bottom.
"""

def square_all_numbers(numbers):
   return[x**2 for x in numbers]


def filter_positive(numbers):
   return[x for x in numbers if x>0]


def double_evens(numbers):
   return[x*2 for x in numbers if x%2==0]


def extract_names(students):
   return[student["name"] for student in students]


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def test_comprehension_builder():
    """Test function with formatted output"""
    print("=" * 60)
    print("SESSION 05 - QUESTION 2: COMPREHENSION BUILDER")
    print("=" * 60)
    print()

    # Test 1: Square all numbers
    print("TEST 1: Square all numbers")
    print("-" * 40)
    numbers = [1, 2, 3, 4, 5]
    squared = square_all_numbers(numbers)
    print(f"Input: {numbers}")
    print(f"Result: {squared}")
    print(f"Expected: [1, 4, 9, 16, 25]")
    print(f"Status: {'✓ PASS' if squared == [1, 4, 9, 16, 25] else '✗ FAIL'}")
    print()

    # Test 2: Filter positive
    print("TEST 2: Keep only positive numbers")
    print("-" * 40)
    mixed_numbers = [-10, 5, -3, 0, 15, -7, 20, 8]
    positive = filter_positive(mixed_numbers)
    print(f"Input: {mixed_numbers}")
    print(f"Result: {positive}")
    print(f"Expected: [5, 15, 20, 8]")
    print(f"Status: {'✓ PASS' if positive == [5, 15, 20, 8] else '✗ FAIL'}")
    print()

    # Test 3: Double evens
    print("TEST 3: Double only the even numbers")
    print("-" * 40)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    doubled_evens = double_evens(numbers)
    print(f"Input: {numbers}")
    print(f"Result: {doubled_evens}")
    print(f"Expected: [4, 8, 12, 16, 20]")
    print(f"Status: {'✓ PASS' if doubled_evens == [4, 8, 12, 16, 20] else '✗ FAIL'}")
    print()

    # Test 4: Extract names
    print("TEST 4: Extract names from student dictionaries")
    print("-" * 40)
    students = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 21},
        {"name": "Charlie", "age": 19},
        {"name": "Diana", "age": 22}
    ]
    names = extract_names(students)
    print(f"Input: {len(students)} student dictionaries")
    print(f"Result: {names}")
    print(f"Expected: ['Alice', 'Bob', 'Charlie', 'Diana']")
    print(f"Status: {'✓ PASS' if names == ['Alice', 'Bob', 'Charlie', 'Diana'] else '✗ FAIL'}")
    print()

    # Bonus examples
    print("=" * 60)
    print("BONUS: More comprehension examples")
    print("=" * 60)

    # Word lengths
    words = ["apple", "banana", "kiwi", "strawberry"]
    lengths = [len(word) for word in words]
    print(f"Word lengths: {lengths}")

    # Filter long words
    long_words = [word for word in words if len(word) >= 6]
    print(f"Long words (>= 6 chars): {long_words}")

    # Uppercase transformation
    upper_words = [word.upper() for word in words]
    print(f"Uppercase: {upper_words}")

    print()
    print("=" * 60)


if __name__ == "__main__":
    test_comprehension_builder()
