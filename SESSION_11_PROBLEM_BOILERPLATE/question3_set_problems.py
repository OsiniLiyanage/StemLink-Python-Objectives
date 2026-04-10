"""
SESSION 11 - QUESTION 3: Set & Hash Map Problems
=================================================
Topics: Set operations, frequency counting, uniqueness problems

Instructions:
1. Implement all 4 functions below
2. Use sets and/or dictionaries (hash maps) for efficient solutions
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def first_unique_char(s):
    """Return the index of the first non-repeating character in s.

    Args:
        s: A string of lowercase letters

    Returns:
        Index of the first character that appears only once, or -1 if none

    Examples:
        first_unique_char("leetcode") -> 0   (l appears once, index 0)
        first_unique_char("loveleetcode") -> 2  (v appears once, index 2)
        first_unique_char("aabb") -> -1      (no unique characters)

    Hint:
        1. Build a frequency dictionary: count how many times each char appears
        2. Loop through the string again to find the first char with count == 1
    """
    # TODO: Build frequency dict, then find first char with count 1
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    for i ,char in enumerate(s):
        if freq[char] ==1:
            return i
    return -1
            
    



def intersection(nums1, nums2):
    """Return a sorted list of elements that appear in both arrays.

    Args:
        nums1: First list of integers
        nums2: Second list of integers

    Returns:
        A sorted list of unique elements present in both arrays

    Examples:
        intersection([1,2,2,1], [2,2]) -> [2]
        intersection([4,9,5], [9,4,9,8,4]) -> [4, 9]

    Hint:
        Convert both to sets and use the & operator, then sort
    """
    # TODO: Use set intersection, return sorted list
    return sorted(set(nums1) & set(nums2))


def has_unique_elements(arr):
    """Return True if all elements in the array are unique.

    Args:
        arr: A list of elements

    Returns:
        True if no duplicates exist, False otherwise

    Examples:
        has_unique_elements([1, 2, 3, 4]) -> True
        has_unique_elements([1, 2, 2, 3]) -> False

    Hint:
        Compare len(arr) with len(set(arr))
    """
    # TODO: Use a set to check for uniqueness
    return len(arr) == len(set(arr))


def find_duplicates(nums):
    """Return a sorted list of elements that appear more than once.

    Args:
        nums: A list of integers

    Returns:
        A sorted list of duplicate elements (each listed once)

    Examples:
        find_duplicates([1, 2, 3, 2, 1, 4]) -> [1, 2]
        find_duplicates([1, 2, 3]) -> []
        find_duplicates([5, 5, 5, 5]) -> [5]

    Hint:
        Build a frequency dict, then collect keys with count > 1
    """
    # TODO: Count frequencies, return sorted list of duplicates
    freq={}
    for num in nums:
        freq[num] = freq.get(num, 0) +1

    result = []
    for num, count in freq.items():
        if count> 1:
            result.append(num)
    return sorted(result)


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 11 - QUESTION 3: SET & HASH MAP PROBLEMS")
    print("=" * 60)

    # Test 1: First unique character
    print("\nTEST 1: First unique character")
    print("-" * 40)
    test_cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("a", 0),
    ]
    for s, expected in test_cases:
        result = first_unique_char(s)
        status = "PASS" if result == expected else "FAIL"
        print(f'  "{s}" -> {result} (Expected: {expected}) {status}')

    # Test 2: Intersection
    print("\nTEST 2: Intersection of two arrays")
    print("-" * 40)
    test_cases = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
        ([1, 2, 3], [4, 5, 6], []),
        ([1, 1, 1], [1, 1, 1], [1]),
    ]
    for nums1, nums2, expected in test_cases:
        result = intersection(nums1, nums2)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {nums1} & {nums2} -> {result} (Expected: {expected}) {status}")

    # Test 3: Has unique elements
    print("\nTEST 3: Has unique elements")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 4], True),
        ([1, 2, 2, 3], False),
        ([], True),
        ([42], True),
        ([1, 1], False),
    ]
    for arr, expected in test_cases:
        result = has_unique_elements(arr)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {arr} -> {result} (Expected: {expected}) {status}")

    # Test 4: Find duplicates
    print("\nTEST 4: Find duplicates")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 2, 1, 4], [1, 2]),
        ([1, 2, 3], []),
        ([5, 5, 5, 5], [5]),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], [1, 5]),
    ]
    for nums, expected in test_cases:
        result = find_duplicates(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {nums} -> {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
