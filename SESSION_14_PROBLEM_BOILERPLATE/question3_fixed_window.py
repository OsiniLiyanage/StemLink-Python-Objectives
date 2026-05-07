"""
SESSION 14 - QUESTION 3: Fixed-Size Sliding Window
==================================================
Topics: Window of size k sliding across the array

Instructions:
1. Implement both functions using the fixed-size sliding window pattern
2. Each slide should be O(1) -- DO NOT recompute the whole sum each time
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def max_sum_subarray(arr, k):
    """Return the maximum sum of any contiguous subarray of size k.

    Args:
        arr: A list of integers
        k: Positive integer window size

    Returns:
        The maximum sum, or -1 if len(arr) < k

    Examples:
        max_sum_subarray([2, 1, 5, 1, 3, 2], 3)  -> 9   (from [5, 1, 3])
        max_sum_subarray([1, 2, 3], 5)           -> -1
        max_sum_subarray([5, 5, 5], 2)           -> 10

    Hint:
        1. If len(arr) < k: return -1
        2. window_sum = sum(arr[:k])
        3. max_sum = window_sum
        4. For i in range(k, len(arr)):
             - window_sum += arr[i] - arr[i - k]
             - max_sum = max(max_sum, window_sum)
        5. Return max_sum
    """
    # TODO: Implement max_sum_subarray with fixed-size sliding window
    pass


def avg_subarrays(arr, k):
    """Return a list of averages for every contiguous subarray of size k.

    Args:
        arr: A list of numbers
        k: Positive integer window size

    Returns:
        A list of floats. Empty list if len(arr) < k.

    Examples:
        avg_subarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
            -> [2.2, 2.8, 2.4, 3.6, 2.8]
        avg_subarrays([1, 2, 3], 5)  -> []

    Hint:
        1. If len(arr) < k: return []
        2. window_sum = sum(arr[:k])
        3. result = [window_sum / k]
        4. For i in range(k, len(arr)):
             - window_sum += arr[i] - arr[i - k]
             - result.append(window_sum / k)
        5. Return result
    """
    # TODO: Implement avg_subarrays with fixed-size sliding window
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 14 - QUESTION 3: FIXED-SIZE SLIDING WINDOW")
    print("=" * 60)

    tests_max = [
        ([2, 1, 5, 1, 3, 2], 3, 9),
        ([1, 2, 3], 5, -1),
        ([5, 5, 5], 2, 10),
        ([1, 2, 3, 4, 5], 2, 9),
        ([-1, -2, -3, -4], 2, -3),
        ([10], 1, 10),
    ]
    for i, (arr, k, expected) in enumerate(tests_max, 1):
        print(f"\nTEST {i}: max_sum_subarray({arr}, {k})")
        print("-" * 40)
        result = max_sum_subarray(arr, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")

    tests_avg = [
        ([1, 3, 2, 6, -1, 4, 1, 8, 2], 5, [2.2, 2.8, 2.4, 3.6, 2.8]),
        ([1, 2, 3], 5, []),
        ([5, 5, 5, 5], 2, [5.0, 5.0, 5.0]),
    ]
    for i, (arr, k, expected) in enumerate(tests_avg, len(tests_max) + 1):
        print(f"\nTEST {i}: avg_subarrays({arr}, {k})")
        print("-" * 40)
        result = avg_subarrays(arr, k)
        ok = result is not None and len(result) == len(expected) and all(
            abs(a - b) < 1e-9 for a, b in zip(result, expected)
        )
        status = "PASS" if ok else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")


if __name__ == "__main__":
    run_tests()
