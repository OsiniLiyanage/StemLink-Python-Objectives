"""
SESSION 11 - QUESTION 4: Group Anagrams (BONUS)
================================================
Topics: Hash map grouping, sorting as keys, advanced patterns

Instructions:
1. Implement all 3 functions below
2. These are more challenging -- take your time!
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def group_anagrams(words):
    """Group words that are anagrams of each other.

    Two words are anagrams if they contain the same characters in any order.
    For example: "eat" and "tea" are anagrams.

    Args:
        words: A list of lowercase strings

    Returns:
        A list of lists, where each inner list contains words that are
        anagrams of each other. Groups should be sorted internally,
        and the overall list should be sorted by the first word in each group.

    Examples:
        group_anagrams(["eat","tea","tan","ate","nat","bat"])
        -> [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]

    Hint:
        1. Use a dictionary where the KEY is tuple(sorted(word))
        2. All anagrams will have the same sorted tuple
        3. Append each word to the list for its key
        4. Sort each group and sort the overall result
    """
    # TODO: Group words by their sorted character tuple
    groups={}
    for word in words:
        key= tuple(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    result =[sorted(group) for group in groups.values()]
    return sorted(result,key=lambda g:g[0])


def two_sum_indices(nums, target):
    """Return indices of two numbers that add up to target.

    Args:
        nums: A list of integers
        target: The target sum

    Returns:
        A list of two indices [i, j] where nums[i] + nums[j] == target
        Return [] if no solution exists
        If multiple solutions exist, return the first one found

    Examples:
        two_sum_indices([2, 7, 11, 15], 9) -> [0, 1]  (2 + 7 = 9)
        two_sum_indices([3, 2, 4], 6) -> [1, 2]  (2 + 4 = 6)

    Hint:
        1. Create a dictionary to store {value: index}
        2. For each number, compute complement = target - num
        3. If complement is in the dictionary, return [dict[complement], i]
        4. Otherwise, add {num: i} to the dictionary
    """
    # TODO: Use a hash map for O(n) two sum
    seen = {}
    for i, num in enumerate(nums):
        complement = target -num
        if complement in seen:
            return [seen[complement],i]
        seen[num] =i
    return []


def subarray_sum_count(nums, k):
    """Count the number of contiguous subarrays that sum to k.

    Args:
        nums: A list of integers
        k: The target sum

    Returns:
        The count of subarrays whose elements sum to k

    Examples:
        subarray_sum_count([1, 1, 1], 2) -> 2
            Subarrays: [1,1] (index 0-1) and [1,1] (index 1-2)

        subarray_sum_count([1, 2, 3], 3) -> 2
            Subarrays: [1,2] (index 0-1) and [3] (index 2)

    Hint (prefix sum + hash map):
        1. Keep a running prefix_sum (cumulative sum)
        2. Keep a dictionary: {prefix_sum_value: count_of_times_seen}
        3. Initialize: prefix_counts = {0: 1}
        4. For each number:
           - Add it to prefix_sum
           - If (prefix_sum - k) is in prefix_counts, add that count to result
           - Add prefix_sum to prefix_counts
        5. Why it works: if prefix_sum[j] - prefix_sum[i] == k,
           then the subarray from i+1 to j sums to k
    """
    # TODO: Use prefix sum + hash map for O(n) solution
    count =0
    prefix_sum =0
    prefix_counts= {0:1}

    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_counts:
            count += prefix_counts[prefix_sum-k]
        prefix_counts[prefix_sum] = prefix_counts.get(prefix_sum,0) +1

    return count


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 11 - QUESTION 4: GROUP ANAGRAMS (BONUS)")
    print("=" * 60)

    # Test 1: Group anagrams
    print("\nTEST 1: Group anagrams")
    print("-" * 40)
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)
    expected = [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    status = "PASS" if result == expected else "FAIL"
    print(f"  {words}")
    print(f"  Groups: {result}")
    print(f"  Expected: {expected}")
    print(f"  Status: {status}")

    words2 = [""]
    result2 = group_anagrams(words2)
    expected2 = [[""]]
    status2 = "PASS" if result2 == expected2 else "FAIL"
    print(f"  {words2} -> {result2} (Expected: {expected2}) {status2}")

    words3 = ["abc", "bca", "xyz", "zyx", "cab"]
    result3 = group_anagrams(words3)
    expected3 = [["abc", "bca", "cab"], ["xyz", "zyx"]]
    status3 = "PASS" if result3 == expected3 else "FAIL"
    print(f"  {words3} -> {result3} (Expected: {expected3}) {status3}")

    # Test 2: Two Sum indices
    print("\nTEST 2: Two Sum indices")
    print("-" * 40)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, expected in test_cases:
        result = two_sum_indices(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  nums={nums}, target={target} -> {result} (Expected: {expected}) {status}")

    result = two_sum_indices([1, 2, 3], 10)
    status = "PASS" if result == [] else "FAIL"
    print(f"  nums=[1,2,3], target=10 -> {result} (Expected: []) {status}")

    # Test 3: Subarray sum count
    print("\nTEST 3: Subarray sum count")
    print("-" * 40)
    test_cases = [
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([1], 1, 1),
        ([1, -1, 1, -1], 0, 4),
    ]
    for nums, k, expected in test_cases:
        result = subarray_sum_count(nums, k)
        status = "PASS" if result == expected else "FAIL"
        print(f"  nums={nums}, k={k} -> {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
