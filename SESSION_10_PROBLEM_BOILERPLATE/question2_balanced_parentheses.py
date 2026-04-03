"""
============================================================
SESSION 10 - QUESTION 2: BALANCED PARENTHESES
============================================================
Topics: Stack application, bracket matching

Instructions:
- This file imports Stack from question1_linked_list_stack.py
- You MUST complete Question 1 first!
- Implement the is_balanced() function using your Stack
- Run this file to test your implementation
- Do NOT modify the test code at the bottom
============================================================
"""

from question1_linked_list_stack import Stack


def is_balanced(expression):
    """
    Check if an expression has balanced parentheses, brackets, and braces.

    Algorithm:
    1. Create a Stack
    2. For each character in the expression:
       - If it's an opening bracket ( [ {: push onto stack
       - If it's a closing bracket ) ] }:
           - If stack is empty: return False (nothing to match)
           - Pop from stack: if it doesn't match, return False
       - If it's any other character: ignore it
    3. Return stack.is_empty()
       (True = all brackets matched, False = unmatched opening brackets)

    Args:
        expression: A string that may contain (, ), [, ], {, }
                    and any other characters (which are ignored)

    Returns:
        True if all brackets are properly matched and nested

    Examples:
        is_balanced("()")         -> True
        is_balanced("({[]})")     -> True
        is_balanced("({[})")      -> False  (] doesn't match {)
        is_balanced("((())")      -> False  (one ( left unmatched)
        is_balanced("")           -> True   (empty is balanced)
        is_balanced("hello")      -> True   (no brackets at all)
        is_balanced("if (x > 0) { return arr[i]; }")  -> True
    """
    # TODO: Create a Stack
    # TODO: Create a matching dictionary: {')': '(', ']': '[', '}': '{'}
    # TODO: For each char in expression:
    #   - If char is in '([{': push onto stack
    #   - If char is in ')]}':
    #       - If stack is empty: return False
    #       - Pop from stack: if popped value != matching[char], return False
    #   - Otherwise: ignore the character
    # TODO: Return stack.is_empty()

    stack = Stack()
    matching = {')': '(', ']': '[', '}': '{'}

    for char in expression:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            if stack.pop() != matching[char]:
                return False
    return stack.is_empty() 
     


# ============================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================

def run_tests():
    print("=" * 60)
    print("SESSION 10 - QUESTION 2: BALANCED PARENTHESES")
    print("=" * 60)

    # Test 1: Balanced expressions
    print("\nTEST 1: Balanced expressions")
    print("-" * 40)
    balanced_tests = [
        ("()", True),
        ("({[]})", True),
        ("([{}])()", True),
        ("", True),
        ("{[()]}", True),
        ("((()))", True),
        ("()()()", True),
        ("{[]}", True),
    ]
    for expr, expected in balanced_tests:
        result = is_balanced(expr)
        status = "PASS" if result == expected else "FAIL"
        display_expr = f'"{expr}"' if expr else '""'
        print(f"  {display_expr} -> {result} (Expected: {expected}) {status}")
    print()

    # Test 2: Unbalanced expressions
    print("TEST 2: Unbalanced expressions")
    print("-" * 40)
    unbalanced_tests = [
        ("({[})", False),
        ("((())", False),
        (")(", False),
        ("(((", False),
        (")))", False),
        ("([)]", False),
        ("({)}", False),
        ("(]", False),
    ]
    for expr, expected in unbalanced_tests:
        result = is_balanced(expr)
        status = "PASS" if result == expected else "FAIL"
        print(f'  "{expr}" -> {result} (Expected: {expected}) {status}')
    print()

    # Test 3: Mixed content (non-bracket characters should be ignored)
    print("TEST 3: Mixed content (ignore non-bracket characters)")
    print("-" * 40)
    mixed_tests = [
        ("if (x > 0) { return arr[i]; }", True),
        ("func(a, b[0])", True),
        ("print('hello')", True),
        ("for i in range(10):", True),
        ("data = {key: [1, 2, 3]}", True),
        ("broken(func[}", False),
        ("no_close(", False),
    ]
    for expr, expected in mixed_tests:
        result = is_balanced(expr)
        status = "PASS" if result == expected else "FAIL"
        print(f'  "{expr}" -> {result} (Expected: {expected}) {status}')
    print()

    # Bonus
    print("=" * 60)
    print("BONUS CHALLENGES:")
    print("-" * 60)
    print("  1. Modify is_balanced to RETURN the position of the first mismatch")
    print("     e.g., is_balanced_verbose('({[})') -> 'Mismatch at position 3'")
    print("  2. Handle string literals: ignore brackets inside quotes")
    print("     e.g., is_balanced('print(\"}\")') should be True")
    print("  3. Write a function that ADDS missing brackets to make an expression balanced")
    print()
    print("  COMPLEXITY ANALYSIS:")
    print("  is_balanced: Time = O(n), Space = O(n)")
    print("  - One pass through the string")
    print("  - Stack can hold at most n/2 opening brackets")


if __name__ == "__main__":
    run_tests()
