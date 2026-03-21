"""
============================================================
SESSION 09 - QUESTION 3: CLASSIC INTERVIEW PROBLEMS
============================================================
Topics: Hash map patterns, Two Sum, stock problem, prefix sums

Instructions:
- Complete each function by replacing 'pass' with your code
- Use efficient O(n) approaches (hash maps, single pass)
- Avoid brute force O(n^2) solutions!
- Run this file to test your implementations
- Do NOT modify the test code at the bottom
============================================================
"""


# ---- FUNCTION 1: Two Sum ----
def two_sum(arr, sum):
    """
    Given an array and a sum, return the indices of two numbers
    that add up to the sum. Use the hash map approach for O(n).

    Args:
        arr: List of integers
        sum: Target sum

    Returns:
        List of two indices [i, j] where arr[i] + arr[j] == sum
        Return empty list if no solution exists

    Examples:
        two_sum([2, 7, 11, 15], 9) -> [0, 1]  (2 + 7 = 9)
        two_sum([3, 2, 4], 6) -> [1, 2]  (2 + 4 = 6)
    """
    # TODO: Use a hash map (dictionary) for O(n) solution
    # Hint: For each number, calculate complement = sum - num
    # Hint: Check if complement is in your num_dict dictionary
    # Hint: Store {value: index} as you go
    num_dict={}
    for i, num in enumerate(arr):
        complement = sum-num
        if complement in num_dict:
            return[num_dict[complement],i]
        num_dict[num]=i
    return[]


# ---- FUNCTION 2: Contains Duplicate ----
def contains_duplicate(nums):
    """
    Return True if any value appears at least twice in the array.

    Args:
        nums: List of integers

    Returns:
        True if duplicates exist, False otherwise

    Examples:
        contains_duplicate([1, 2, 3, 1]) -> True
        contains_duplicate([1, 2, 3, 4]) -> False
    """
    # TODO: Use a hash set for O(n) solution
    # Hint: Add each number to a set
    # Hint: If the number is already in the set, return True
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    
        
    


# ---- FUNCTION 3: Best Time to Buy and Sell Stock ----
def max_profit(prices):
    """
    Find the maximum profit from buying and selling a stock once.
    You must buy before you sell. Return 0 if no profit is possible.

    Args:
        prices: List of daily stock prices

    Returns:
        Maximum profit (integer)

    Examples:
        max_profit([7, 1, 5, 3, 6, 4]) -> 5  (buy at 1, sell at 6)
        max_profit([7, 6, 4, 3, 1]) -> 0  (prices only decrease)
    """
    # TODO: Single-pass approach tracking minimum price
    # Hint: Track the minimum price seen so far
    # Hint: At each price, calculate profit if we sold today
    # Hint: Update max_profit if this profit is better
    if not prices:
        return 0
    min_price =prices[0]
    best =0
    for price in prices:
        min_price = min(min_price,price)
        best = max(best,price - min_price)
    return best


# ---- FUNCTION 4: Prefix Sum Range Queries ----
def prefix_sum_range(arr, queries):
    """
    Given an array and a list of range queries [start, end],
    return the sum for each query using prefix sums.

    Args:
        arr: List of integers
        queries: List of [start, end] pairs (inclusive)

    Returns:
        List of sums, one for each query

    Examples:
        prefix_sum_range([1, 2, 3, 4, 5], [[0, 2], [1, 3], [0, 4]])
        -> [6, 9, 15]
        # [0,2]: 1+2+3=6, [1,3]: 2+3+4=9, [0,4]: 1+2+3+4+5=15
    """
    # TODO: Build prefix sum array, then answer queries in O(1) each
    # Step 1: Build prefix array where prefix[i] = sum(arr[0..i])
    # Step 2: For query [start, end]:
    #   If start == 0: answer = prefix[end]
    #   Else: answer = prefix[end] - prefix[start - 1]
    prefix =[0]* len(arr)
    prefix[0] = arr[0]
    for i in range(1,len(arr)):
        prefix[i]=prefix[i-1]+arr[i]

    results = []
    for start, end in queries:
        if start ==0:
            results.append(prefix[end])
        else:
            results.append(prefix[end]-prefix[start-1])
    return results


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 09 - QUESTION 3: CLASSIC INTERVIEW PROBLEMS")
    print("=" * 60)

    # Test 1: Two Sum
    print("\nTEST 1: Two Sum")
    print("-" * 40)
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 5, 3, 7], 8, [1, 2]),
        ([2, 7, 11, 15], 18, [1, 2]),
    ]
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        status = "PASS" if result == expected else "FAIL"
        print(f"  arr={nums}, sum={target} -> {result} (Expected: {expected}) {status}")
    print()

    # Test 2: Contains Duplicate
    print("TEST 2: Contains Duplicate")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
    ]
    for nums, expected in test_cases:
        result = contains_duplicate(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"  {nums} -> {result} (Expected: {expected}) {status}")
    print()

    # Test 3: Best Time to Buy and Sell Stock
    print("TEST 3: Best time to buy and sell stock")
    print("-" * 40)
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2], 1),
        ([2, 1, 4], 3),
        ([3, 3, 3], 0),
    ]
    for prices, expected in test_cases:
        result = max_profit(prices)
        status = "PASS" if result == expected else "FAIL"
        print(f"  prices={prices} -> {result} (Expected: {expected}) {status}")
    print()

    # Test 4: Prefix Sum Range Queries
    print("TEST 4: Prefix sum range queries")
    print("-" * 40)
    test_cases = [
        ([1, 2, 3, 4, 5], [[0, 2], [1, 3], [0, 4]], [6, 9, 15]),
        ([10, 20, 30], [[0, 0], [0, 2], [1, 2]], [10, 60, 50]),
        ([5, 5, 5, 5], [[0, 3], [1, 2]], [20, 10]),
    ]
    for arr, queries, expected in test_cases:
        result = prefix_sum_range(arr, queries)
        status = "PASS" if result == expected else "FAIL"
        print(f"  arr={arr}")
        print(f"  queries={queries}")
        print(f"  result={result}")
        print(f"  expected={expected}")
        print(f"  Status: {status}")
        print()

    # Bonus
    print("=" * 60)
    print("BONUS: Complexity Analysis")
    print("-" * 60)
    print("  1. two_sum:           Time = O(n), Space = O(n)")
    print("  2. contains_duplicate: Time = O(n), Space = O(n)")
    print("  3. max_profit:        Time = O(n), Space = O(1)")
    print("  4. prefix_sum_range:  Time = O(n + q), Space = O(n)")
    print("     (n = array size, q = number of queries)")
    print()
    print("  Why is hash map Two Sum better than brute force?")
    print("  Brute force: O(n^2) -- check every pair")
    print("  Hash map: O(n) -- one pass with O(1) lookups")


if __name__ == "__main__":
    run_tests()
