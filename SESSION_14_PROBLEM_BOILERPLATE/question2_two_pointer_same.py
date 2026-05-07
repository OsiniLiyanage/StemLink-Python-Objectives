"""
SESSION 14 - QUESTION 2: Two-Pointer (Same Direction + Container)
=================================================================
Topics: Read/write two-pointer, container with most water

Instructions:
1. Implement both functions
2. Run this file to test your implementation
3. Do NOT modify the test code below the line
"""


def remove_duplicates(nums):
    """Remove duplicates in-place from a sorted array. Return the new length k.
    The first k elements of nums (after the call) should be the unique values
    in their original order. Elements beyond index k don't matter.

    Args:
        nums: A sorted list of integers (modified in place)

    Returns:
        Integer k = number of unique elements

    Examples:
        nums = [1, 1, 2, 3, 3]
        k = remove_duplicates(nums)
        # k = 3
        # nums[:3] == [1, 2, 3]

    Hint:
        1. If nums is empty, return 0
        2. write = 1
        3. For read in range(1, len(nums)):
             - if nums[read] != nums[write - 1]:
                 nums[write] = nums[read]
                 write += 1
        4. Return write
    """
    # TODO: Implement remove_duplicates with same-direction two-pointer
    pass


def max_area(heights):
    """Given a list of bar heights, find the maximum amount of water that can
    be contained between any two bars.

    Area = (right_index - left_index) * min(heights[left], heights[right])

    Args:
        heights: A list of non-negative integers

    Returns:
        The maximum area as an integer

    Examples:
        max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])  -> 49
        max_area([1, 1])                       -> 1
        max_area([4, 3, 2, 1, 4])              -> 16

    Hint:
        1. left, right = 0, len(heights) - 1
        2. max_water = 0
        3. While left < right:
             - width = right - left
             - height = min(heights[left], heights[right])
             - max_water = max(max_water, width * height)
             - Move the pointer at the shorter side inward
        4. Return max_water
    """
    # TODO: Implement max_area with opposite-direction two-pointer
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 14 - QUESTION 2: TWO-POINTER (SAME DIR + CONTAINER)")
    print("=" * 60)

    # remove_duplicates tests
    tests_dedup = [
        ([1, 1, 2, 3, 3], 3, [1, 2, 3]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 1, 1, 1], 1, [1]),
        ([], 0, []),
        ([5], 1, [5]),
    ]
    for i, (nums, expected_k, expected_prefix) in enumerate(tests_dedup, 1):
        arr = list(nums)
        print(f"\nTEST {i}: remove_duplicates({nums})")
        print("-" * 40)
        k = remove_duplicates(arr)
        ok = (k == expected_k) and (arr[:expected_k] == expected_prefix)
        status = "PASS" if ok else "FAIL"
        print(f"  k:        {k} (Expected: {expected_k})")
        print(f"  Prefix:   {arr[:expected_k] if k is not None else None} (Expected: {expected_prefix})")
        print(f"  Status: {status}")

    # max_area tests
    tests_area = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
    ]
    for i, (heights, expected) in enumerate(tests_area, len(tests_dedup) + 1):
        print(f"\nTEST {i}: max_area({heights})")
        print("-" * 40)
        result = max_area(heights)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")


if __name__ == "__main__":
    run_tests()
