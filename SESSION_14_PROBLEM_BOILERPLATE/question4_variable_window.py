"""
SESSION 14 - QUESTION 4: Variable-Size Sliding Window
=====================================================
Topics: Window that grows and shrinks based on a condition

Instructions:
1. Implement both functions using the variable-size sliding window pattern
2. Use a `while` loop (not `if`) for the shrink step
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def min_subarray_len(target, nums):
    """Return the length of the smallest contiguous subarray with sum >= target.
    Return 0 if no such subarray exists.

    Args:
        target: A positive integer target sum
        nums: A list of positive integers

    Returns:
        Length of the smallest qualifying subarray, or 0 if none

    Examples:
        min_subarray_len(7, [2, 3, 1, 2, 4, 3])  -> 2  (from [4, 3])
        min_subarray_len(4, [1, 4, 4])           -> 1  (from [4])
        min_subarray_len(11, [1, 1, 1, 1])       -> 0

    Hint:
        1. min_len = float('inf')
        2. window_sum = 0
        3. left = 0
        4. For right in range(len(nums)):
             - window_sum += nums[right]         # expand
             - while window_sum >= target:       # shrink while valid
                 min_len = min(min_len, right - left + 1)
                 window_sum -= nums[left]
                 left += 1
        5. Return min_len if min_len != float('inf') else 0
    """
    # TODO: Implement min_subarray_len with variable-size sliding window
    min_len = float('inf')
    window_sum = 0
    left=0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            min_len = min(min_len, right-left+1)
            window_sum -= nums[left]
            left+=1

    return min_len if min_len != float('inf') else 0


def length_of_longest_substring(s):
    """Return the length of the longest substring of s with all unique
    characters.

    Args:
        s: A string

    Returns:
        Length of the longest substring with no repeated characters

    Examples:
        length_of_longest_substring("abcabcbb")  -> 3   ("abc")
        length_of_longest_substring("bbbbb")     -> 1   ("b")
        length_of_longest_substring("pwwkew")    -> 3   ("wke")
        length_of_longest_substring("")          -> 0

    Hint:
        1. char_set = set()
        2. left = 0
        3. max_len = 0
        4. For right in range(len(s)):
             - while s[right] in char_set:     # shrink while INVALID
                 char_set.remove(s[left])
                 left += 1
             - char_set.add(s[right])          # expand (now valid)
             - max_len = max(max_len, right - left + 1)
        5. Return max_len
    """
    # TODO: Implement length_of_longest_substring with variable-size window
    

    char_set = set()
    left=0
    max_len =0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left +=1

        char_set.add(s[right])
        max_len = max(max_len,right-left+1)
    return max_len


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 14 - QUESTION 4: VARIABLE-SIZE SLIDING WINDOW")
    print("=" * 60)

    tests_min = [
        (7, [2, 3, 1, 2, 4, 3], 2),
        (4, [1, 4, 4], 1),
        (11, [1, 1, 1, 1], 0),
        (15, [1, 2, 3, 4, 5], 5),
        (5, [5], 1),
    ]
    for i, (target, nums, expected) in enumerate(tests_min, 1):
        print(f"\nTEST {i}: min_subarray_len({target}, {nums})")
        print("-" * 40)
        result = min_subarray_len(target, nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")

    tests_str = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("dvdf", 3),
        ("abcdef", 6),
    ]
    for i, (s, expected) in enumerate(tests_str, len(tests_min) + 1):
        print(f"\nTEST {i}: length_of_longest_substring({s!r})")
        print("-" * 40)
        result = length_of_longest_substring(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")


if __name__ == "__main__":
    run_tests()
