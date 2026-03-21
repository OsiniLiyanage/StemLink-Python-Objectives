"""
============================================================
SESSION 09 - QUESTION 4: ARRAY CHALLENGE (BONUS)
============================================================
Topics: Kadane's algorithm, advanced array patterns

Instructions:
- These are more challenging problems -- take your time!
- Complete each function by replacing 'pass' with your code
- Think about the pattern BEFORE coding
- Run this file to test your implementations
- Do NOT modify the test code at the bottom
============================================================
"""


# ---- FUNCTION 1: Maximum Subarray (Kadane's Algorithm) ----
def max_subarray(nums):
    """
    Find the contiguous subarray with the largest sum.
    Use Kadane's algorithm.

    The key insight: at each element, decide:
    "Is it better to START FRESH here, or EXTEND the current subarray?"

    Args:
        nums: List of integers (can include negatives)

    Returns:
        Maximum subarray sum (integer)

    Examples:
        max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
        # Subarray [4, -1, 2, 1] has sum 6
        max_subarray([1]) -> 1
        max_subarray([-1, -2, -3]) -> -1  (least negative)
    """
    # TODO: Implement Kadane's algorithm
    # Hint: Track curr_sum and max_sum
    # Hint: curr_sum = max(nums[i], curr_sum + nums[i])
    # Hint: max_sum = max(max_sum, curr_sum)
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num,curr_sum + num)
        max_sum = max(max_sum,curr_sum)
    return max_sum



# ---- FUNCTION 2: Product Except Self ----
def product_except_self(nums):
    """
    Return an array where each element is the product of all
    other elements. Do NOT use division!

    Args:
        nums: List of integers

    Returns:
        List where result[i] = product of all nums except nums[i]

    Examples:
        product_except_self([1, 2, 3, 4]) -> [24, 12, 8, 6]
        product_except_self([2, 3, 4, 5]) -> [60, 40, 30, 24]
    """
    # TODO: Two-pass approach (left products, then right products)
    # Pass 1 (left to right): result[i] = product of everything LEFT of i
    # Pass 2 (right to left): multiply result[i] by product of everything RIGHT of i
    #
    # Example walkthrough for [1, 2, 3, 4]:
    # After pass 1: [1, 1, 2, 6]     (left products)
    # After pass 2: [24, 12, 8, 6]   (multiply by right products)
    n= len(nums)
    result =[1] * n
 
    left =1
    for i in range(n):
        result[i]=left
        left *= nums[i]

    right =1
    for i in range(n - 1,-1, -1):
        result[i] *= right
        right *= nums[i]
    return result


# ---- FUNCTION 3: Merge Two Sorted Arrays ----
def merge_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays into one sorted array.
    Use the two-pointer technique.

    Args:
        arr1: First sorted list
        arr2: Second sorted list

    Returns:
        New sorted list containing all elements from both arrays

    Examples:
        merge_sorted_arrays([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
        merge_sorted_arrays([1, 2, 3], []) -> [1, 2, 3]
    """
    # TODO: Use two pointers, one for each array
    # Hint: Compare elements at both pointers
    # Hint: Add the smaller one to result, advance that pointer
    # Hint: When one array is exhausted, add remaining from the other
    result =[]
    i = j=0
    while i< len(arr1) and j< len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j +=1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result


# ---- FUNCTION 4: Find Missing Number ----
def find_missing_number(nums):
    """
    Given an array containing n distinct numbers from the range [0, n],
    find the one number that is missing.

    Use the math trick: expected_sum - actual_sum = missing number

    Args:
        nums: List of n distinct integers from range [0, n]

    Returns:
        The missing number

    Examples:
        find_missing_number([3, 0, 1]) -> 2  (range [0, 3], missing 2)
        find_missing_number([0, 1]) -> 2  (range [0, 2], missing 2)
        find_missing_number([9,6,4,2,3,5,7,0,1]) -> 8
    """
    # TODO: Use the sum formula: n * (n + 1) / 2
    # Hint: n = len(nums) (since one number is missing from [0, n])
    # Hint: expected_sum = n * (n + 1) // 2
    # Hint: actual_sum = sum(nums)
    # Hint: missing = expected_sum - actual_sum
    n = len(nums)
    expected = n*(n+1) //2
    return expected - sum(nums)


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 09 - QUESTION 4: ARRAY CHALLENGE")
    print("=" * 60)

    # Test 1: Maximum subarray
    print("\nTEST 1: Maximum subarray (Kadane's algorithm)")
    print("-" * 40)
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([-1, -2, -3], -1),
        ([5, 4, -1, 7, 8], 23),
        ([-2, -1], -1),
        ([1, 2, 3, 4], 10),
    ]
    for nums, expected in test_cases:
        result = max_subarray(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {nums} -> {result} (Expected: {expected}) {status}")
    print()

    # Test 2: Product except self
    print("TEST 2: Product except self (no division!)")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([2, 3, 4, 5], [60, 40, 30, 24]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]
    for nums, expected in test_cases:
        result = product_except_self(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {nums} -> {result} (Expected: {expected}) {status}")
    print()

    # Test 3: Merge sorted arrays
    print("TEST 3: Merge two sorted arrays")
    print("-" * 40)
    test_cases = [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], [4, 5, 6], [4, 5, 6]),
        ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
        ([1, 5, 9], [2, 3, 7, 10], [1, 2, 3, 5, 7, 9, 10]),
    ]
    for arr1, arr2, expected in test_cases:
        result = merge_sorted_arrays(arr1, arr2)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {arr1} + {arr2} -> {result} (Expected: {expected}) {status}")
    print()

    # Test 4: Find missing number
    print("TEST 4: Find missing number")
    print("-" * 40)
    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
    ]
    for nums, expected in test_cases:
        result = find_missing_number(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {nums} -> {result} (Expected: {expected}) {status}")
    print()

    # Bonus
    print("=" * 60)
    print("BONUS: Complexity Analysis")
    print("-" * 60)
    print("  1. max_subarray:        Time = O(n), Space = O(1)")
    print("  2. product_except_self: Time = O(n), Space = O(n)")
    print("  3. merge_sorted_arrays: Time = O(n+m), Space = O(n+m)")
    print("  4. find_missing_number: Time = O(n), Space = O(1)")
    print()
    print("  CHALLENGE: Can you solve product_except_self with O(1) extra space?")
    print("  (The output array doesn't count as extra space)")


if __name__ == "__main__":
    run_tests()
