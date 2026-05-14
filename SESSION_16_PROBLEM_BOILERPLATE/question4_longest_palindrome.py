"""
SESSION 16 - QUESTION 4: Longest Palindromic Substring (BONUS)
==============================================================
Topics: String manipulation, expand-around-center

Instructions:
1. Implement longest_palindrome using the expand-around-center approach
2. O(n^2) time, O(1) extra space
3. Run this file to test your implementation
4. Do NOT modify the test code below the line
"""


def longest_palindrome(s):
    """Return the longest palindromic substring of s.

    A palindrome reads the same forwards and backwards (e.g. "aba", "abba").
    If multiple longest palindromes exist, return any one of them.

    Args:
        s: A string

    Returns:
        The longest palindromic substring

    Examples:
        longest_palindrome("babad")  -> "bab" or "aba"
        longest_palindrome("cbbd")   -> "bb"
        longest_palindrome("a")      -> "a"
        longest_palindrome("ac")     -> "a" or "c"
        longest_palindrome("")       -> ""

    Strategy: expand around center
        For each index, try expanding outward as long as the chars match.
        Two cases per index:
          - odd-length palindrome centered at i        -> expand(i, i)
          - even-length palindrome centered between i and i+1
                                                       -> expand(i, i+1)

    Hint:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        result = ""
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)
            if len(odd) > len(result):  result = odd
            if len(even) > len(result): result = even
        return result
    """
    # TODO: Implement longest_palindrome with expand-around-center
    pass


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def is_palindrome(s):
    return s == s[::-1]


def run_tests():
    print("=" * 60)
    print("SESSION 16 - QUESTION 4: LONGEST PALINDROMIC SUBSTRING")
    print("=" * 60)

    # (input, expected_length, list_of_acceptable_answers)
    cases = [
        ("babad", 3, ["bab", "aba"]),
        ("cbbd",  2, ["bb"]),
        ("a",     1, ["a"]),
        ("ac",    1, ["a", "c"]),
        ("",      0, [""]),
        ("racecar", 7, ["racecar"]),
        ("forgeeksskeegfor", 10, ["geeksskeeg"]),
        ("aacabdkacaa", 3, ["aca"]),
    ]

    for i, (s, expected_len, accepted) in enumerate(cases, 1):
        print(f"\nTEST {i}: longest_palindrome({s!r})")
        print("-" * 40)
        result = longest_palindrome(s)
        # Accept any longest palindrome of correct length, or one of the accepted answers
        if result is None:
            status = "FAIL"
        else:
            ok = (len(result) == expected_len
                  and (result in s or result == "")
                  and is_palindrome(result))
            status = "PASS" if ok else "FAIL"
        print(f"  Result:   {result!r}")
        print(f"  Expected length: {expected_len}, e.g. {accepted}")
        print(f"  Status: {status}")


if __name__ == "__main__":
    run_tests()
