"""
SESSION 15 - QUESTION 1: DP Basics
==================================
Topics: Memoization, tabulation, space optimization

Instructions:
1. Implement all three functions
2. Each must be O(n) time. fib_optimized must be O(1) space.
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def climb_stairs(n):
    """Number of distinct ways to climb n stairs taking 1 or 2 steps at a time.

    Args:
        n: Non-negative integer (number of stairs)

    Returns:
        Number of distinct ways to reach the top

    Examples:
        climb_stairs(2)  -> 2   (1+1, 2)
        climb_stairs(3)  -> 3
        climb_stairs(5)  -> 8

    Hint:
        1. If n <= 2: return n
        2. dp = [0] * (n + 1)
        3. dp[1], dp[2] = 1, 2
        4. For i from 3 to n: dp[i] = dp[i-1] + dp[i-2]
        5. Return dp[n]
    """
    # TODO: Implement climb_stairs with tabulation
    
    if n <= 2:
        return n
    dp = [0] * (n+1)
    dp[1],dp[2] = 1,2
    for i in range(3,n+1):
        dp[i] = dp[i-1] +dp[i-2]
    return dp[n]



def fib_memo(n, memo=None):
    """The n-th Fibonacci number using memoization. Must be O(n).

    fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)

    Args:
        n: Non-negative integer
        memo: Internal cache (do NOT pass it from outside)

    Returns:
        The n-th Fibonacci number

    Examples:
        fib_memo(0)  -> 0
        fib_memo(1)  -> 1
        fib_memo(10) -> 55
        fib_memo(50) -> 12586269025

    Hint:
        1. If memo is None: memo = {}
        2. If n in memo: return memo[n]
        3. If n <= 1: return n
        4. memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        5. Return memo[n]
    """
    # TODO: Implement fib_memo with memoization
    
    if memo is None:
        memo= {}
    if n in memo:
        return memo[n]
    if n<= 1:
            return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]


def fib_optimized(n):
    """The n-th Fibonacci number in O(n) time and O(1) space.

    Only keep the last two values, not the whole array.

    Args:
        n: Non-negative integer

    Returns:
        The n-th Fibonacci number

    Examples:
        fib_optimized(0)  -> 0
        fib_optimized(1)  -> 1
        fib_optimized(10) -> 55

    Hint:
        1. If n <= 1: return n
        2. prev2, prev1 = 0, 1
        3. For _ in range(2, n+1):
             curr = prev1 + prev2
             prev2 = prev1
             prev1 = curr
        4. Return prev1
    """
    # TODO: Implement fib_optimized with O(1) space
    if n <= 1:
        return n
    prev2,prev1 =0,1
    for _ in range(2,n+1):
        curr = prev1+prev2
        prev2 = prev1
        prev1 = curr
    return prev1


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 15 - QUESTION 1: DP BASICS")
    print("=" * 60)

    stairs_tests = [(1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (10, 89)]
    for i, (n, expected) in enumerate(stairs_tests, 1):
        print(f"\nTEST {i}: climb_stairs({n})")
        print("-" * 40)
        result = climb_stairs(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")

    fib_memo_tests = [(0, 0), (1, 1), (2, 1), (10, 55), (20, 6765), (50, 12586269025)]
    for i, (n, expected) in enumerate(fib_memo_tests, len(stairs_tests) + 1):
        print(f"\nTEST {i}: fib_memo({n})")
        print("-" * 40)
        result = fib_memo(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")

    fib_opt_tests = [(0, 0), (1, 1), (2, 1), (10, 55), (30, 832040)]
    for i, (n, expected) in enumerate(fib_opt_tests, len(stairs_tests) + len(fib_memo_tests) + 1):
        print(f"\nTEST {i}: fib_optimized({n})")
        print("-" * 40)
        result = fib_optimized(n)
        status = "PASS" if result == expected else "FAIL"
        print(f"  Result: {result} (Expected: {expected}) {status}")


if __name__ == "__main__":
    run_tests()
