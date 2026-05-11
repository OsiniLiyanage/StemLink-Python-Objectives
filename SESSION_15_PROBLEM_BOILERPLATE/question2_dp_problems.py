"""
SESSION 15 - QUESTION 2: DP Problems
====================================
Topics: Coin change, house robber

Instructions:
1. Implement both functions using DP
2. Apply the 5-step recipe: state, recurrence, base, order, answer
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def coin_change(coins, amount):
    """Minimum number of coins needed to make `amount`. Return -1 if impossible.

    Args:
        coins: List of distinct positive integer denominations
        amount: Non-negative integer target

    Returns:
        Minimum number of coins, or -1 if no combination works

    Examples:
        coin_change([1, 5, 10, 25], 30)  -> 2     (25 + 5)
        coin_change([2], 3)              -> -1
        coin_change([1, 2, 5], 11)       -> 3     (5 + 5 + 1)
        coin_change([1], 0)              -> 0

    Hint:
        1. dp = [infinity] * (amount + 1)
        2. dp[0] = 0
        3. For i from 1 to amount:
             For each coin:
               If coin <= i:
                 dp[i] = min(dp[i], dp[i - coin] + 1)
        4. Return dp[amount] if dp[amount] != infinity else -1

    State:      dp[i] = min coins to make amount i
    Recurrence: dp[i] = min(dp[i - coin] + 1) over all coins where coin <= i
    Base:       dp[0] = 0
    """
    # TODO: Implement coin_change with tabulation
    dp = [float('inf')]* (amount+1)
    dp[0] =0
    for i in range(1,amount+1):
        for coin in coins:
            if coin <=1:
                dp[i] = min(dp[i],dp[i-coin]+1)
    return dp[amount] if dp[amount] != float('inf') else -1






def house_robber(nums):
    """Maximum money you can rob from a row of houses without robbing two
    adjacent houses.

    Args:
        nums: List of non-negative integers (money in each house)

    Returns:
        Maximum amount of money

    Examples:
        house_robber([1, 2, 3, 1])         -> 4    (rob houses 0 and 2)
        house_robber([2, 7, 9, 3, 1])      -> 12   (rob houses 0, 2, 4)
        house_robber([])                   -> 0
        house_robber([5])                  -> 5
        house_robber([2, 1])               -> 2

    Hint:
        1. If not nums: return 0
        2. If len(nums) == 1: return nums[0]
        3. dp = [0] * len(nums)
        4. dp[0] = nums[0]
        5. dp[1] = max(nums[0], nums[1])
        6. For i from 2 to len(nums) - 1:
             dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        7. Return dp[-1]

    State:      dp[i] = max money from houses 0..i
    Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    Base:       dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
    """
    # TODO: Implement house_robber with tabulation
    if not nums:
        return 0
    if len(nums) ==1:
        return nums[0]
    dp = [0] *len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0],nums[1])
    for i in range(2,len(nums)):
        dp[i] =max(dp[i-1],dp[i-2]+nums[i])
    return dp[-1]


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 15 - QUESTION 2: DP PROBLEMS")
    print("=" * 60)

    coin_tests = [
        ([1, 5, 10, 25], 30, 2),
        ([2], 3, -1),
        ([1, 2, 5], 11, 3),
        ([1], 0, 0),
        ([1, 3, 4], 6, 2),
        ([2, 5, 10, 1], 27, 4),
    ]
    for i, (coins, amount, expected) in enumerate(coin_tests, 1):
        print(f"\nTEST {i}: coin_change({coins}, {amount})")
        print("-" * 40)
        result = coin_change(coins, amount)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")

    rob_tests = [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([], 0),
        ([5], 5),
        ([2, 1], 2),
        ([2, 1, 1, 2], 4),
        ([10, 1, 1, 10], 20),
    ]
    for i, (nums, expected) in enumerate(rob_tests, len(coin_tests) + 1):
        print(f"\nTEST {i}: house_robber({nums})")
        print("-" * 40)
        result = house_robber(nums)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
