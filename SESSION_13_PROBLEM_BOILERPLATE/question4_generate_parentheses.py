"""
SESSION 13 - QUESTION 4: Generate Parentheses (BONUS)
=====================================================
Topics: Backtracking with constraints

Instructions:
1. Implement generate_parentheses using the backtracking pattern
2. This is a bonus challenge -- trace through n=2 on paper first!
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def generate_parentheses(n):
    """Generate all valid combinations of n pairs of parentheses.

    A valid combination has:
    - Exactly n opening '(' and n closing ')' parentheses
    - At every point, the number of ')' never exceeds the number of '('

    Args:
        n: Number of pairs of parentheses

    Returns:
        A sorted list of all valid combinations

    Examples:
        generate_parentheses(1) -> ["()"]
        generate_parentheses(2) -> ["(())", "()()"]
        generate_parentheses(3) -> ["((()))", "(()())", "(())()", "()(())", "()()()"]

    Hint:
        1. Create result = []
        2. Define backtrack(current, open_count, close_count):
           - If len(current) == 2 * n: append current to result, return
           - If open_count < n:
             - backtrack(current + "(", open_count + 1, close_count)
           - If close_count < open_count:
             - backtrack(current + ")", open_count, close_count + 1)
        3. Call backtrack("", 0, 0)
        4. Return sorted result
    """
    # TODO: Implement generate_parentheses with backtracking
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 13 - QUESTION 4: GENERATE PARENTHESES (BONUS)")
    print("=" * 60)

    # Test 1: n=1
    print("\nTEST 1: generate_parentheses(1)")
    print("-" * 40)
    result = generate_parentheses(1)
    expected = ["()"]
    status = "PASS" if result == expected else "FAIL"
    print(f"  Result: {result} (Expected: {expected}) {status}")

    # Test 2: n=2
    print("\nTEST 2: generate_parentheses(2)")
    print("-" * 40)
    result = generate_parentheses(2)
    expected = ["(())", "()()"]
    status = "PASS" if result == expected else "FAIL"
    print(f"  Result: {result} (Expected: {expected}) {status}")

    # Test 3: n=3
    print("\nTEST 3: generate_parentheses(3)")
    print("-" * 40)
    result = generate_parentheses(3)
    expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    status = "PASS" if result == expected else "FAIL"
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Status: {status}")

    # Test 4: n=4 count (Catalan number C_4 = 14)
    print("\nTEST 4: generate_parentheses(4) -- count should be 14")
    print("-" * 40)
    result = generate_parentheses(4)
    status = "PASS" if len(result) == 14 else "FAIL"
    print(f"  Count: {len(result)} (Expected: 14) {status}")

    # Test 5: n=5 count (Catalan number C_5 = 42)
    print("\nTEST 5: generate_parentheses(5) -- count should be 42")
    print("-" * 40)
    result = generate_parentheses(5)
    status = "PASS" if len(result) == 42 else "FAIL"
    print(f"  Count: {len(result)} (Expected: 42) {status}")


if __name__ == "__main__":
    run_tests()
