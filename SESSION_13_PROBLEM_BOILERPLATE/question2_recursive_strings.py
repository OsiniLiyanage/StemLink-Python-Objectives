"""
SESSION 13 - QUESTION 2: Recursive Strings & Lists
===================================================
Topics: String recursion, palindrome, flatten nested list

Instructions:
1. Implement all 3 functions using recursion (no loops!)
2. Run this file to test your implementation
3. Do NOT modify the test code below the line
"""


def reverse_string(s):
    """Reverse a string using recursion.

    Args:
        s: A string

    Returns:
        The reversed string

    Examples:
        reverse_string("hello") -> "olleh"
        reverse_string("a") -> "a"
        reverse_string("") -> ""

    Hint:
        Base case: if len(s) <= 1, return s
        Recursive case: return reverse_string(s[1:]) + s[0]
        (reverse the rest, then append the first character at the end)
    """
    # TODO: Implement reverse_string recursively
    pass


def is_palindrome(s):
    """Check if a string is a palindrome using recursion.

    A palindrome reads the same forwards and backwards.

    Args:
        s: A string

    Returns:
        True if s is a palindrome, False otherwise

    Examples:
        is_palindrome("racecar") -> True
        is_palindrome("hello") -> False
        is_palindrome("a") -> True
        is_palindrome("") -> True

    Hint:
        Base case: if len(s) <= 1, return True
        If s[0] != s[-1], return False
        Recursive case: return is_palindrome(s[1:-1])
    """
    # TODO: Implement is_palindrome recursively
    pass


def flatten(nested_list):
    """Flatten a nested list into a single flat list using recursion.

    Args:
        nested_list: A list that may contain other lists (nested arbitrarily deep)

    Returns:
        A single flat list with all elements

    Examples:
        flatten([1, [2, 3], [4, [5, 6]], 7]) -> [1, 2, 3, 4, 5, 6, 7]
        flatten([[1, 2], [3, 4]]) -> [1, 2, 3, 4]
        flatten([1, 2, 3]) -> [1, 2, 3]

    Hint:
        Create a result list.
        For each item in nested_list:
            If isinstance(item, list): extend result with flatten(item)
            Else: append item to result
        Return result
    """
    # TODO: Implement flatten recursively
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 13 - QUESTION 2: RECURSIVE STRINGS & LISTS")
    print("=" * 60)

    # Test 1: Reverse string
    print("\nTEST 1: Reverse string")
    print("-" * 40)
    test_cases = [
        ("hello", "olleh"),
        ("a", "a"),
        ("", ""),
        ("abcdef", "fedcba"),
        ("racecar", "racecar"),
    ]
    for s, expected in test_cases:
        result = reverse_string(s)
        status = "PASS" if result == expected else "FAIL"
        print(f'  reverse_string("{s}") -> "{result}" (Expected: "{expected}") {status}')

    # Test 2: Is palindrome
    print("\nTEST 2: Is palindrome")
    print("-" * 40)
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("a", True),
        ("", True),
        ("abba", True),
        ("abcd", False),
        ("madam", True),
    ]
    for s, expected in test_cases:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f'  is_palindrome("{s}") -> {result} (Expected: {expected}) {status}')

    # Test 3: Flatten
    print("\nTEST 3: Flatten nested list")
    print("-" * 40)
    test_cases = [
        ([1, [2, 3], [4, [5, 6]], 7], [1, 2, 3, 4, 5, 6, 7]),
        ([[1, 2], [3, 4]], [1, 2, 3, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
        ([[[1]], [[2]], [[3]]], [1, 2, 3]),
        ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
    ]
    for nested, expected in test_cases:
        result = flatten(nested)
        status = "PASS" if result == expected else "FAIL"
        print(f"  flatten({nested}) -> {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
