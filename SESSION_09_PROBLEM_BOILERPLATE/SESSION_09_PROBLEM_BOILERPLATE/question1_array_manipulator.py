"""
============================================================
SESSION 09 - QUESTION 1: ARRAY MANIPULATOR
============================================================
Topics: In-place array operations, two pointers, read/write pointer

Instructions:
- Complete each function by replacing 'pass' with your code
- Do NOT use built-in reverse(), sort(), or slicing tricks like [::-1]
- The goal is to implement the algorithms yourself!
- Run this file to test your implementations
- Do NOT modify the test code at the bottom
============================================================
"""


# ---- FUNCTION 1: Reverse In-Place ----
def reverse_in_place(arr):
    """
    Reverse the array in-place using two pointers.
    Do NOT use arr.reverse() or arr[::-1].

    Args:
        arr: List of elements to reverse

    Returns:
        The same list, reversed in-place

    Example:
        reverse_in_place([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
    """
    # TODO: Use two pointers (left and right) to swap elements
    # Hint: left starts at 0, right starts at len(arr) - 1
    # Hint: Swap arr[left] and arr[right], then move pointers inward
    left,right = 0,len(arr)-1
    while left< right:
        arr[left],arr[right]= arr[right],arr[left]
        left +=1
        right -= 1
    return arr


# ---- FUNCTION 2: Move Zeros ----
def move_zeros(arr):
    """
    Move all zeros to the end of the array while maintaining
    the relative order of non-zero elements. Do it in-place.

    Args:
        arr: List of integers

    Returns:
        The same list with zeros moved to the end

    Example:
        move_zeros([0, 1, 0, 3, 12]) -> [1, 3, 12, 0, 0]
    """
    # TODO: Use the read/write pointer pattern
    # Hint: 'write' tracks where to place the next non-zero
    # Hint: 'read' scans through every element
    # Hint: If arr[read] != 0, swap arr[write] and arr[read], then advance write

    write =0
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write],arr[read] = arr[read], arr[write]
            write+= 1
    return arr

    


# ---- FUNCTION 3: Remove Duplicates from Sorted Array ----
def remove_duplicates_sorted(arr):
    """
    Remove duplicates from a SORTED array in-place.
    Return the new length of the unique portion.

    Args:
        arr: Sorted list of integers (may contain duplicates)

    Returns:
        Integer: the number of unique elements

    Example:
        remove_duplicates_sorted([1, 1, 2, 2, 3, 4, 4, 5]) -> 5
        (arr is now [1, 2, 3, 4, 5, ...] -- first 5 elements are unique)
    """
    # TODO: Use the read/write pointer pattern
    # Hint: write starts at 1 (first element is always unique)
    # Hint: If arr[read] != arr[write - 1], it's a new unique element
    if not arr:
        return 0
    write =1
    for read in range(1,len(arr)):
        if arr[read] != arr[write-1]:
            arr[write]= arr[read]
            write+=1
    return write



# ---- FUNCTION 4: Rotate Right ----
def rotate_right(arr, k):
    """
    Rotate the array RIGHT by k positions using the
    "three reverses" trick. Do it in-place.

    In class we saw LEFT rotation:
        reverse(arr, 0, n)      # Reverse all
        reverse(arr, n-k, n)    # Reverse last k
        reverse(arr, 0, n-k)    # Reverse first n-k

    For RIGHT rotation, the reverse order changes!

    Args:
        arr: List of elements to rotate
        k: Number of positions to rotate right

    Returns:
        The same list, rotated right by k positions

    Example:
        rotate_right([1, 2, 3, 4, 5, 6, 7], 3) -> [5, 6, 7, 1, 2, 3, 4]
    """
    # TODO: Implement three-reverses for RIGHT rotation
    # Step 0: Handle k > len(arr) with k = k % len(arr)
    # Step 1: Reverse the entire array
    # Step 2: Reverse the first k elements
    # Step 3: Reverse the remaining (n - k) elements
    # Hint: Write a helper: reverse(arr, left, right) with right EXCLUSIVE
    #       (do right -= 1 first, then two-pointer swap)
    def reverse(arr,left,right):
        right -= 1
        while left< right:
            arr[left],arr[right]= arr[right], arr[left]
            left +=1
            right -=1
    
    n= len(arr)
    if n ==0:
        return arr

    k = k % n
    reverse(arr,0,n)
    reverse(arr,0,k)
    reverse(arr,k,n)
    return arr


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 09 - QUESTION 1: ARRAY MANIPULATOR")
    print("=" * 60)

    # Test 1: Reverse in-place
    print("\nTEST 1: Reverse array in-place")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
        ([10, 20, 30, 40], [40, 30, 20, 10]),
    ]
    for arr, expected in test_cases:
        original = arr.copy()
        result = reverse_in_place(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Input: {original}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")
        print()

    # Test 2: Move zeros
    print("TEST 2: Move zeros to end")
    print("-" * 40)
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 0, 1], [1, 0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0], [0]),
        ([1, 0, 2, 0, 3, 0], [1, 2, 3, 0, 0, 0]),
    ]
    for arr, expected in test_cases:
        original = arr.copy()
        result = move_zeros(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Input: {original}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")
        print()

    # Test 3: Remove duplicates from sorted array
    print("TEST 3: Remove duplicates from sorted array")
    print("-" * 40)
    test_cases = [
        ([1, 1, 2, 2, 3, 4, 4, 5], 5),
        ([1, 1, 1, 1], 1),
        ([1, 2, 3, 4, 5], 5),
        ([1], 1),
        ([1, 1, 2], 2),
    ]
    for arr, expected_len in test_cases:
        original = arr.copy()
        result_len = remove_duplicates_sorted(arr)
        status = "PASS" if result_len == expected_len else "FAIL"
        print(f"  Input: {original}")
        print(f"  New length: {result_len}")
        if result_len is not None:
            print(f"  Unique portion: {arr[:result_len]}")
        print(f"  Expected length: {expected_len}")
        print(f"  Status: {status}")
        print()

    # Test 4: Rotate right
    print("TEST 4: Rotate array right by k positions")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([1, 2, 3], 1, [3, 1, 2]),
        ([1, 2, 3], 3, [1, 2, 3]),
        ([1, 2], 5, [2, 1]),
        ([1], 10, [1]),
    ]
    for arr, k, expected in test_cases:
        original = arr.copy()
        result = rotate_right(arr, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Input: {original}, k={k}")
        print(f"  Result: {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")
        print()


if __name__ == "__main__":
    run_tests()
