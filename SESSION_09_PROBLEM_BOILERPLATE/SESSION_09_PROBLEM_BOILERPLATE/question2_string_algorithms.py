"""
============================================================
SESSION 09 - QUESTION 2: STRING ALGORITHMS
============================================================
Topics: String traversal, two pointers, frequency counting

Instructions:
- Complete each function by replacing 'pass' with your code
- Use efficient approaches (two pointers, frequency maps)
- Remember: strings are immutable in Python -- use lists for building
- Run this file to test your implementations
- Do NOT modify the test code at the bottom
============================================================
"""


# ---- FUNCTION 1: Palindrome Check ----
def is_palindrome(word):
    """
    Check if a word is a palindrome using two pointers.
    Compare characters directly (no normalization needed).

    Args:
        word: String to check

    Returns:
        True if palindrome, False otherwise

    Examples:
        is_palindrome("racecar") -> True
        is_palindrome("hello") -> False
        is_palindrome("madam") -> True
    """
    # TODO: Use two pointers (left and right)
    # Hint: left starts at 0, right starts at len(word) - 1
    # Hint: Compare characters from both ends moving inward
    # Hint: If any pair doesn't match, return False
    left,right = 0, len(word)-1
    while left< right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


# ---- FUNCTION 2: Anagram Check ----
def is_anagram(word1, word2):
    """
    Check if two strings are anagrams using frequency counting.

    Args:
        word1: First string
        word2: Second string

    Returns:
        True if anagrams, False otherwise

    Examples:
        is_anagram("listen", "silent") -> True
        is_anagram("hello", "world") -> False
        is_anagram("triangle", "integral") -> True
    """
    # TODO: Use frequency counting with a dictionary
    # Hint: If lengths differ, they can't be anagrams
    # Hint: Count character frequencies in word1 using freq.get(char, 0) + 1
    # Hint: For word2, check if freq.get(char, 0) == 0 (means char missing/exhausted)
    # Hint: Decrement freq[char] for each character in word2
    if len(word1) != len(word2):
        return False
    freq ={}
    for char in word1:
        freq[char]=freq.get(char,0)+1
    for char in word2:
        if freq.get(char,0)==0:
            return False
        freq[char] -= 1
    return True


# ---- FUNCTION 3: String Compression ----
def compress_string(s):
    """
    Compress a string by counting consecutive repeated characters.
    If the compressed string is NOT shorter, return the original.

    Args:
        s: String to compress

    Returns:
        Compressed string, or original if compression doesn't help

    Examples:
        compress_string("aabcccccaaa") -> "a2b1c5a3"
        compress_string("abc") -> "abc" (compressed "a1b1c1" is longer)
        compress_string("aabb") -> "aabb" (compressed "a2b2" is same length)
    """
    # TODO: Build compressed string using a list
    # Hint: Track current character and its count
    # Hint: When character changes, append char + count to result list
    # Hint: Don't forget the last group!
    # Hint: Use ''.join(result) at the end
    # Hint: Return original if compressed is not shorter
    if not s:
        return s
    result =[]
    current = s[0]
    count =1

    for i in range(1,len(s)):
        if s[i]== current:
            count +=1
        else:
            result.append(current+str(count))
            current = s[i]
            count=1
    result.append(current+str(count))
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s
    


# ---- FUNCTION 4: First Unique Character ----
def first_unique_char(s):
    """
    Find the index of the first non-repeating character in a string.
    Return -1 if no unique character exists.

    Args:
        s: String to search

    Returns:
        Index of first unique character, or -1

    Examples:
        first_unique_char("leetcode") -> 0  ('l' appears once)
        first_unique_char("loveleetcode") -> 2  ('v' appears once)
        first_unique_char("aabb") -> -1  (no unique characters)
    """
    # TODO: Two-pass approach using frequency counting
    # Pass 1: Count frequency of each character
    # Pass 2: Find first character with count == 1
    freq ={}
    for char in s:
         freq[char] = freq.get(char,0)+1
    for i,char in enumerate(s):
        if freq[char] ==1:
            return i
    return -1


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 09 - QUESTION 2: STRING ALGORITHMS")
    print("=" * 60)

    # Test 1: Palindrome check
    print("\nTEST 1: Palindrome check")
    print("-" * 40)
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("noon", True),
        ("car", False),
        ("civic", True),
        ("", True),
        ("a", True),
        ("ab", False),
    ]
    for s, expected in test_cases:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        print(f'  "{s}" -> {result} (Expected: {expected}) {status}')
    print()

    # Test 2: Anagram check
    print("TEST 2: Anagram check")
    print("-" * 40)
    test_cases = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("triangle", "integral", True),
        ("dusty", "study", True),
        ("rat", "car", False),
        ("silent", "listens", False),
        ("", "", True),
    ]
    for s1, s2, expected in test_cases:
        result = is_anagram(s1, s2)
        status = "PASS" if result == expected else "FAIL"
        print(f'  "{s1}" vs "{s2}" -> {result} (Expected: {expected}) {status}')
    print()

    # Test 3: String compression
    print("TEST 3: String compression")
    print("-" * 40)
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abc", "abc"),
        ("aabb", "aabb"),
        ("aaaa", "a4"),
        ("a", "a"),
        ("aab", "aab"),
        ("aaabbbccc", "a3b3c3"),
    ]
    for s, expected in test_cases:
        result = compress_string(s)
        status = "PASS" if result == expected else "FAIL"
        print(f'  "{s}" -> "{result}" (Expected: "{expected}") {status}')
    print()

    # Test 4: First unique character
    print("TEST 4: First unique character")
    print("-" * 40)
    test_cases = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("abcabc", -1),
        ("abcdef", 0),
        ("aabbc", 4),
        ("", -1),
    ]
    for s, expected in test_cases:
        result = first_unique_char(s)
        status = "PASS" if result == expected else "FAIL"
        print(f'  "{s}" -> {result} (Expected: {expected}) {status}')
    print()

    # Bonus: Complexity analysis
    print("=" * 60)
    print("BONUS: What is the time and space complexity of each function?")
    print("-" * 60)
    print("  1. is_palindrome:    Time = ?, Space = ?")
    print("  2. is_anagram:       Time = ?, Space = ?")
    print("  3. compress_string:  Time = ?, Space = ?")
    print("  4. first_unique_char:Time = ?, Space = ?")
    print()
    print("  Answers: All are O(n) time!")
    print("  Space: palindrome=O(1), anagram=O(k), compress=O(n), unique=O(k)")
    print("  k = number of unique characters (bounded by alphabet size)")


if __name__ == "__main__":
    run_tests()
