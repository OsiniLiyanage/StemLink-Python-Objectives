"""
SESSION 16 - QUESTION 1: Complexity Analysis & Optimization
===========================================================
Topics: Big O, hash maps, recognizing nested loops

Instructions:
1. Implement both versions of count_pairs (brute and fast)
2. count_pairs_brute must be O(n^2). count_pairs_fast must be O(n).
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def count_pairs_brute(nums, k):
    """Count unordered pairs (i < j) such that nums[i] + nums[j] == k.

    Use nested loops. O(n^2) time, O(1) space.

    Args:
        nums: List of integers
        k:    Target sum

    Returns:
        Number of qualifying pairs

    Examples:
        count_pairs_brute([1, 5, 7, -1, 5], 6)  -> 3   (1+5, 1+5, 7+-1)
        count_pairs_brute([1, 1, 1, 1], 2)      -> 6
        count_pairs_brute([], 5)                -> 0

    Hint:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k:
                    count += 1
        return count
    """
    # TODO: Implement count_pairs_brute (nested loops)
    pass


def count_pairs_fast(nums, k):
    """Count unordered pairs (i < j) such that nums[i] + nums[j] == k.

    Use a hash map. O(n) time, O(n) space.

    For each new num, the partner we need is k - num. Look up how many
    times we've already seen that partner; that's how many pairs end
    here.

    Args:
        nums: List of integers
        k:    Target sum

    Returns:
        Number of qualifying pairs

    Examples:
        count_pairs_fast([1, 5, 7, -1, 5], 6)  -> 3
        count_pairs_fast([1, 1, 1, 1], 2)      -> 6

    Hint:
        seen = {}
        count = 0
        for num in nums:
            count += seen.get(k - num, 0)
            seen[num] = seen.get(num, 0) + 1
        return count
    """
    # TODO: Implement count_pairs_fast (hash map)
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 16 - QUESTION 1: COMPLEXITY ANALYSIS")
    print("=" * 60)

    cases = [
        ([1, 5, 7, -1, 5], 6, 3),
        ([1, 1, 1, 1], 2, 6),
        ([], 5, 0),
        ([1, 2, 3], 10, 0),
        ([0, 0, 0], 0, 3),
        ([5, 5, 5, 5, 5], 10, 10),
        ([-2, 1, 3, 4], 2, 1),
    ]
    for i, (nums, k, expected) in enumerate(cases, 1):
        print(f"\nTEST {i}: count_pairs_brute({nums}, {k})")
        print("-" * 40)
        result = count_pairs_brute(nums, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")

    for i, (nums, k, expected) in enumerate(cases, len(cases) + 1):
        print(f"\nTEST {i}: count_pairs_fast({nums}, {k})")
        print("-" * 40)
        result = count_pairs_fast(nums, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
