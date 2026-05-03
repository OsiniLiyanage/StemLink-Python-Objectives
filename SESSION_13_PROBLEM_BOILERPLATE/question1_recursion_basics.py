"""
SESSION 13 - QUESTION 1: Recursion Basics
==========================================
Topics: Base cases, recursive cases, call stack

Instructions:
1. Implement all 4 recursive functions below
2. Each function MUST use recursion (no loops!)
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def factorial(n):
    """Return n! (n factorial) using recursion.

    Args:
        n: A non-negative integer

    Returns:
        n! = n * (n-1) * (n-2) * ... * 1

    Examples:
        factorial(5) -> 120
        factorial(0) -> 1
        factorial(1) -> 1

    Hint:
        Base case: if n <= 1, return 1
        Recursive case: return n * factorial(n - 1)
    """
    # TODO: Implement factorial recursively
    pass


def fibonacci(n):
    """Return the n-th Fibonacci number using recursion.

    Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

    Args:
        n: A non-negative integer (0-indexed)

    Returns:
        The n-th Fibonacci number

    Examples:
        fibonacci(0) -> 0
        fibonacci(1) -> 1
        fibonacci(6) -> 8

    Hint:
        Base cases: fib(0) = 0, fib(1) = 1
        Recursive case: fib(n-1) + fib(n-2)
    """
    # TODO: Implement fibonacci recursively
    pass


def power(base, exp):
    """Return base raised to the power exp using recursion.

    Args:
        base: The base number
        exp: The exponent (non-negative integer)

    Returns:
        base^exp

    Examples:
        power(2, 10) -> 1024
        power(3, 4) -> 81
        power(5, 0) -> 1

    Hint:
        Base case: if exp == 0, return 1
        Recursive case: return base * power(base, exp - 1)
    """
    # TODO: Implement power recursively
    pass


def recursive_sum(arr):
    """Return the sum of all elements in arr using recursion.

    Args:
        arr: A list of numbers

    Returns:
        The sum of all elements

    Examples:
        recursive_sum([1, 2, 3, 4, 5]) -> 15
        recursive_sum([]) -> 0
        recursive_sum([42]) -> 42

    Hint:
        Base case: if arr is empty, return 0
        Recursive case: return arr[0] + recursive_sum(arr[1:])
    """
    # TODO: Implement sum recursively
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 13 - QUESTION 1: RECURSION BASICS")
    print("=" * 60)

    # Test 1: Factorial
    print("\nTEST 1: Factorial")
    print("-" * 40)
    test_cases = [
        (0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (10, 3628800),
    ]
    for n, expected in test_cases:
        result = factorial(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"  factorial({n}) -> {result} (Expected: {expected}) {status}")

    # Test 2: Fibonacci
    print("\nTEST 2: Fibonacci")
    print("-" * 40)
    test_cases = [
        (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (10, 55),
    ]
    for n, expected in test_cases:
        result = fibonacci(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"  fibonacci({n}) -> {result} (Expected: {expected}) {status}")

    # Test 3: Power
    print("\nTEST 3: Power")
    print("-" * 40)
    test_cases = [
        (2, 0, 1), (2, 1, 2), (2, 10, 1024), (3, 4, 81), (5, 3, 125),
    ]
    for base, exp, expected in test_cases:
        result = power(base, exp)
        status = "PASS" if result == expected else "FAIL"
        print(f"  power({base}, {exp}) -> {result} (Expected: {expected}) {status}")

    # Test 4: Recursive sum
    print("\nTEST 4: Recursive sum")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 4, 5], 15),
        ([], 0),
        ([42], 42),
        ([10, -10, 20, -20], 0),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10),
    ]
    for arr, expected in test_cases:
        result = recursive_sum(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"  recursive_sum({arr}) -> {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
