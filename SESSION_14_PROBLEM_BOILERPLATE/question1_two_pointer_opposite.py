"""
SESSION 14 - QUESTION 1: Two-Pointer (Opposite Direction)
=========================================================
Topics: Pointers moving toward each other on a sorted array

Instructions:
1. Implement both functions using the opposite-direction two-pointer pattern
2. Run this file to test your implementation
3. Do NOT modify the test code below the line
"""


def two_sum_sorted(nums, target):
    """Given a sorted array, return [left, right] indices of the two numbers
    that add up to target. Return [] if no such pair exists.

    Args:
        nums: A sorted list of integers
        target: An integer target sum

    Returns:
        [left, right] indices (left < right), or [] if none found

    Examples:
        two_sum_sorted([2, 7, 11, 15], 9)  -> [0, 1]
        two_sum_sorted([1, 3, 5, 7], 12)   -> [2, 3]
        two_sum_sorted([1, 2, 3], 10)      -> []

    Hint:
        1. left = 0, right = len(nums) - 1
        2. while left < right:
             - current_sum = nums[left] + nums[right]
             - if current_sum == target: return [left, right]
             - elif current_sum < target: left += 1
             - else: right -= 1
        3. return []
    """
    # TODO: Implement two_sum_sorted with opposite-direction two-pointer
    left,right =0, len(nums) -1

    while left< right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return[left,right]
        elif current_sum < target:
            left +=1
        else:
            right -=1
    return []



def is_valid_palindrome(s):
    """Return True if s is a palindrome, considering only alphanumeric
    characters and ignoring case.

    Args:
        s: A string

    Returns:
        True if valid palindrome, False otherwise

    Examples:
        is_valid_palindrome("A man, a plan, a canal: Panama")  -> True
        is_valid_palindrome("race a car")                       -> False
        is_valid_palindrome("")                                 -> True

    Hint:
        1. left, right = 0, len(s) - 1
        2. while left < right:
             - skip non-alphanumeric from left: while left<right and not s[left].isalnum(): left+=1
             - skip non-alphanumeric from right: while left<right and not s[right].isalnum(): right-=1
             - if s[left].lower() != s[right].lower(): return False
             - left += 1; right -= 1
        3. return True
    """
    # TODO: Implement is_valid_palindrome with opposite-direction two-pointer
    
    left,right =0, len(s) -1
    while left <right:
        while left< right and not s[left].isalnum():
            left +=1
        while left< right and not s[right].isalnum():
            right -=1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -=1
    return True


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 14 - QUESTION 1: TWO-POINTER (OPPOSITE)")
    print("=" * 60)

    # Two Sum tests
    tests_two_sum = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([1, 3, 5, 7], 12, [2, 3]),
        ([1, 2, 3], 10, []),
        ([-3, -1, 0, 2, 5], 2, [1, 4]),
        ([1, 2], 3, [0, 1]),
    ]
    for i, (nums, target, expected) in enumerate(tests_two_sum, 1):
        print(f"\nTEST {i}: two_sum_sorted({nums}, {target})")
        print("-" * 40)
        result = two_sum_sorted(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")

    # Palindrome tests
    tests_pal = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        ("racecar", True),
        (".,", True),
        ("0P", False),
    ]
    for i, (s, expected) in enumerate(tests_pal, len(tests_two_sum) + 1):
        print(f"\nTEST {i}: is_valid_palindrome({s!r})")
        print("-" * 40)
        result = is_valid_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result:   {result}")
        print(f"  Expected: {expected}")
        print(f"  Status: {status}")


if __name__ == "__main__":
    run_tests()
