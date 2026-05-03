"""
SESSION 13 - QUESTION 3: Generate Subsets
=========================================
Topics: Backtracking, generating all subsets of a list

Instructions:
1. Implement generate_subsets using the backtracking pattern
2. Remember: Choose -> Explore -> Un-choose
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def generate_subsets(nums):
    """Generate all possible subsets of nums using backtracking.

    Args:
        nums: A list of distinct integers

    Returns:
        A list of all subsets (each subset is a list)

    Examples:
        generate_subsets([1, 2, 3]) ->
            [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]

    Hint:
        1. Create result = []
        2. Define backtrack(start, current):
           a. Append current[:] to result (every path is a valid subset!)
           b. For i in range(start, len(nums)):
              - current.append(nums[i])      # Choose
              - backtrack(i + 1, current)     # Explore (move forward!)
              - current.pop()                 # Un-choose
        3. Call backtrack(0, [])
        4. Return result

    IMPORTANT: Save current[:] (a copy), NOT current itself!
    """
    # TODO: Implement generate_subsets with backtracking
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 13 - QUESTION 3: GENERATE SUBSETS")
    print("=" * 60)

    # Test 1: Subsets of [1, 2, 3]
    print("\nTEST 1: Subsets of [1, 2, 3]")
    print("-" * 40)
    result = generate_subsets([1, 2, 3])
    expected = [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    status = "PASS" if result == expected else "FAIL"
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Status: {status}")

    # Test 2: Subsets of [1, 2]
    print("\nTEST 2: Subsets of [1, 2]")
    print("-" * 40)
    result = generate_subsets([1, 2])
    expected = [[], [1], [1, 2], [2]]
    status = "PASS" if result == expected else "FAIL"
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Status: {status}")

    # Test 3: Subsets of empty list
    print("\nTEST 3: Subsets of []")
    print("-" * 40)
    result = generate_subsets([])
    expected = [[]]
    status = "PASS" if result == expected else "FAIL"
    print(f"  Result:   {result}")
    print(f"  Expected: {expected}")
    print(f"  Status: {status}")

    # Test 4: Subset count for [1,2,3,4] should be 2^4 = 16
    print("\nTEST 4: Subset count for [1,2,3,4] should be 2^4 = 16")
    print("-" * 40)
    result = generate_subsets([1, 2, 3, 4])
    status = "PASS" if len(result) == 16 else "FAIL"
    print(f"  Count: {len(result)} (Expected: 16) {status}")

    # Test 5: Subset count for [1,2,3,4,5] should be 2^5 = 32
    print("\nTEST 5: Subset count for [1,2,3,4,5] should be 2^5 = 32")
    print("-" * 40)
    result = generate_subsets([1, 2, 3, 4, 5])
    status = "PASS" if len(result) == 32 else "FAIL"
    print(f"  Count: {len(result)} (Expected: 32) {status}")


if __name__ == "__main__":
    run_tests()
