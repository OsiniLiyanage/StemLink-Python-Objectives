"""
SESSION 16 - QUESTION 2: Two Sum -- Both Ways
=============================================
Topics: Time-space trade-offs, hash maps

Instructions:
1. Implement BOTH versions
2. two_sum_brute is O(n^2) time / O(1) space
3. two_sum_hash is O(n) time / O(n) space
4. Run this file to test your implementation
5. Do NOT modify the test code below the line

Note: assume exactly one solution exists, and the array is unsorted.
"""


def two_sum_brute(nums, target):
    """Return [i, j] (i < j) such that nums[i] + nums[j] == target.

    Use nested loops. O(n^2) time, O(1) space.

    Args:
        nums:   List of integers (unsorted)
        target: Integer

    Returns:
        [i, j] indices of the two numbers that sum to target

    Examples:
        two_sum_brute([2, 7, 11, 15], 9)  -> [0, 1]
        two_sum_brute([3, 2, 4], 6)       -> [1, 2]
        two_sum_brute([3, 3], 6)          -> [0, 1]

    Hint:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    """
    # TODO: Implement two_sum_brute
    pass


def two_sum_hash(nums, target):
    """Return [i, j] (i < j) such that nums[i] + nums[j] == target.

    Use a hash map. O(n) time, O(n) space.

    For each element nums[i], ask: has target - nums[i] appeared before?

    Args:
        nums:   List of integers (unsorted)
        target: Integer

    Returns:
        [i, j] indices

    Examples:
        two_sum_hash([2, 7, 11, 15], 9)  -> [0, 1]

    Hint:
        seen = {}                       # value -> index
        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
    """
    # TODO: Implement two_sum_hash
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 16 - QUESTION 2: TWO SUM -- BOTH WAYS")
    print("=" * 60)

    cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
    ]
    for i, (nums, target, expected) in enumerate(cases, 1):
        print(f"\nTEST {i}: two_sum_brute({nums}, {target})")
        print("-" * 40)
        result = two_sum_brute(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")

    for i, (nums, target, expected) in enumerate(cases, len(cases) + 1):
        print(f"\nTEST {i}: two_sum_hash({nums}, {target})")
        print("-" * 40)
        result = two_sum_hash(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
