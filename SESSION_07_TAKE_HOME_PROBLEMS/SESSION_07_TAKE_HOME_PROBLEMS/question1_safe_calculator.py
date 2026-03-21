"""
SESSION 07 - Question 1: Safe Calculator
Topics: Error handling, try/except, input validation

INSTRUCTIONS:
Complete the four functions below. Replace 'pass' with your code.
Run this file to test your implementation.
"""
from typing import Optional


def safe_divide(a: float, b: float) -> Optional[float]:
    """
    Safely divide a by b with error handling.

    Args:
        a: Dividend (numerator)
        b: Divisor (denominator)

    Returns:
        float: The result of a/b, or None if error occurs

    Example:
        safe_divide(10, 2)  # Returns 5.0
        safe_divide(10, 0)  # Returns None (ZeroDivisionError)
        safe_divide("10", 2)  # Returns None (TypeError)
    """
    # TODO: Implement with try/except for ZeroDivisionError and TypeError
    
    try:
        return a/b
    except(ZeroDivisionError,TypeError):
        return None


def safe_convert(value:str, target_type: type):
    """
    Safely convert a value to a target type.

    Args:
        value: The value to convert
        target_type: The type to convert to (int, float, str)

    Returns:
        The converted value, or None if conversion fails

    Example:
        safe_convert("42", int)    # Returns 42
        safe_convert("abc", int)   # Returns None (ValueError)
        safe_convert("3.14", float)  # Returns 3.14
    """
    # TODO: Implement with try/except for ValueError
    try:
        return target_type(value)
    except(ValueError,TypeError):
        return None
   


def get_valid_number(prompt: str) -> int:
    """
    Get a valid number from user input with validation loop.

    Args:
        prompt (str): The prompt to display to user

    Returns:
        int: A valid integer entered by the user

    Example:
        number = get_valid_number("Enter age: ")
        # If user types "abc", asks again
        # If user types "25", returns 25
    """
    # TODO: Implement with while True + try/except
    # Keep asking until user enters a valid number
    # Return the number when valid input is received
    while True:
        try:
            valid_number = input(prompt)
            return  int(valid_number)
        except ValueError:
            print("Invalid Number.please ender a valid one.")
        


def safe_list_access(lst:list, index: int):
    """
    Safely access a list element with error handling.

    Args:
        lst: The list to access
        index: The index to access

    Returns:
        The element at lst[index], or None if index is out of range

    Example:
        safe_list_access([1, 2, 3], 1)   # Returns 2
        safe_list_access([1, 2, 3], 10)  # Returns None (IndexError)
    """
    # TODO: Implement with try/except for IndexError
    try:
        return lst[index]
    except IndexError:
        return None



# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_safe_divide():
    """Test safe_divide function"""
    print("="*60)
    print("TESTING SAFE DIVIDE")
    print("="*60)

    # Test 1: Normal division
    result = safe_divide(10, 2)
    if result == 5.0:
        print("✓ PASS: safe_divide(10, 2) = 5.0")
    else:
        print(f"✗ FAIL: Expected 5.0, got {result}")

    # Test 2: Division by zero
    result = safe_divide(10, 0)
    if result is None:
        print("✓ PASS: safe_divide(10, 0) returns None (no crash!)")
    else:
        print(f"✗ FAIL: Expected None, got {result}")

    # Test 3: Type error
    result = safe_divide("10", 2)
    if result is None:
        print("✓ PASS: safe_divide('10', 2) returns None (TypeError)")
    else:
        print(f"✗ FAIL: Expected None, got {result}")

    # Test 4: Float division
    result = safe_divide(7, 2)
    if result == 3.5:
        print("✓ PASS: safe_divide(7, 2) = 3.5")
    else:
        print(f"✗ FAIL: Expected 3.5, got {result}")

    print()


def test_safe_convert():
    """Test safe_convert function"""
    print("="*60)
    print("TESTING SAFE CONVERT")
    print("="*60)

    # Test 1: String to int
    result = safe_convert("42", int)
    if result == 42:
        print("✓ PASS: safe_convert('42', int) = 42")
    else:
        print(f"✗ FAIL: Expected 42, got {result}")

    # Test 2: Invalid int conversion
    result = safe_convert("abc", int)
    if result is None:
        print("✓ PASS: safe_convert('abc', int) returns None (ValueError)")
    else:
        print(f"✗ FAIL: Expected None, got {result}")

    # Test 3: String to float
    result = safe_convert("3.14", float)
    if result == 3.14:
        print("✓ PASS: safe_convert('3.14', float) = 3.14")
    else:
        print(f"✗ FAIL: Expected 3.14, got {result}")

    # Test 4: String to string
    result = safe_convert(42, str)
    if result == "42":
        print("✓ PASS: safe_convert(42, str) = '42'")
    else:
        print(f"✗ FAIL: Expected '42', got {result}")

    print()


def test_safe_list_access():
    """Test safe_list_access function"""
    print("="*60)
    print("TESTING SAFE LIST ACCESS")
    print("="*60)

    test_list = [10, 20, 30, 40, 50]

    # Test 1: Valid index
    result = safe_list_access(test_list, 2)
    if result == 30:
        print("✓ PASS: safe_list_access([10,20,30,40,50], 2) = 30")
    else:
        print(f"✗ FAIL: Expected 30, got {result}")

    # Test 2: Out of range index
    result = safe_list_access(test_list, 10)
    if result is None:
        print("✓ PASS: safe_list_access(..., 10) returns None (IndexError)")
    else:
        print(f"✗ FAIL: Expected None, got {result}")

    # Test 3: Negative index (should work!)
    result = safe_list_access(test_list, -1)
    if result == 50:
        print("✓ PASS: safe_list_access(..., -1) = 50 (last element)")
    else:
        print(f"✗ FAIL: Expected 50, got {result}")

    # Test 4: First element
    result = safe_list_access(test_list, 0)
    if result == 10:
        print("✓ PASS: safe_list_access(..., 0) = 10")
    else:
        print(f"✗ FAIL: Expected 10, got {result}")

    print()


if __name__ == "__main__":
    test_safe_divide()
    test_safe_convert()
    test_safe_list_access()

    print("="*60)
    print("TESTS COMPLETE")
    print("="*60)
    print("\n💡 TIP: Implement all functions to pass all tests!")
    print("💡 TIP: Use specific exception types (ValueError, TypeError, etc)")
