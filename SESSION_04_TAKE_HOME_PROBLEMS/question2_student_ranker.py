"""
SESSION 04 - QUESTION 2: STUDENT RANKER
========================================

Topics Covered: zip(), enumerate(), sorted() with key parameter

TASK:
Complete the three functions below to manage and rank student data.
All the printing and formatting is handled for you - just implement the logic!

DO NOT modify the test code at the bottom.
"""

def create_student_records(names, scores, ages):
    """
    Use zip() to combine three lists into a list of tuples.
    Each tuple should be: (name, score, age)

    Args:
        names: list of student names (strings)
        scores: list of test scores (integers)
        ages: list of ages (integers)

    Returns:
        list of tuples: [(name, score, age), ...]

    Example:
        create_student_records(['Alice', 'Bob'], [85, 90], [20, 21])
        should return [('Alice', 85, 20), ('Bob', 90, 21)]
    """
    return list(zip(names,scores,ages))

    # TODO: Implement using zip() and convert to list
    pass


def rank_by_score(student_records):
    """
    Use sorted() with a lambda key to sort students by score (highest first).

    Args:
        student_records: list of tuples [(name, score, age), ...]

    Returns:
        list of tuples sorted by score in descending order

    Example:
        rank_by_score([('Alice', 85, 20), ('Bob', 90, 21)])
        should return [('Bob', 90, 21), ('Alice', 85, 20)]
    """
    return sorted(student_records,key=lambda score:score[1],reverse=True)

    # TODO: Implement using sorted() with key parameter and reverse=True
    # Hint: Each tuple is (name, score, age), so score is at index 1
    pass


def print_numbered_list(student_records):
    """
    Use enumerate() to print a numbered list starting from 1.

    Args:
        student_records: list of tuples [(name, score, age), ...]

    Returns:
        list of formatted strings in this format:
        ["1. Alice (age 20): 85 points", "2. Bob (age 21): 90 points", ...]

    Example:
        print_numbered_list([('Alice', 85, 20)])
        should return ["1. Alice (age 20): 85 points"]
    """
    # TODO: Implement using enumerate() with start=1
    # Create a list of formatted strings
    result = []
    for rank, student in enumerate(student_records, start=1):
        name,score,age = student
        corrected = f"{rank}. {name} (age {age}): {score} points"
        result.append(corrected)
    return result

    # Your code here

    


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def test_student_ranker():
    """Test function with formatted output"""
    print("=" * 60)
    print("SESSION 04 - QUESTION 2: STUDENT RANKER")
    print("=" * 60)

    # Test data
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    scores = [85, 92, 78, 95, 88]
    ages = [20, 21, 19, 22, 20]

    print("\nInput Data:")
    print(f"Names:  {names}")
    print(f"Scores: {scores}")
    print(f"Ages:   {ages}")
    print()

    # Test 1: Create student records
    print("TEST 1: Create student records using zip()")
    print("-" * 40)
    records = create_student_records(names, scores, ages)
    print(f"Result: {records}")
    expected_records = [('Alice', 85, 20), ('Bob', 92, 21), ('Charlie', 78, 19),
                       ('Diana', 95, 22), ('Eve', 88, 20)]
    print(f"Expected: {expected_records}")
    print(f"Status: {'✓ PASS' if records == expected_records else '✗ FAIL'}")
    print()

    # Test 2: Rank by score
    print("TEST 2: Rank students by score (highest first)")
    print("-" * 40)
    ranked = rank_by_score(records)
    print("Result:")
    for student in ranked:
        print(f"  {student[0]}: {student[1]} points")
    expected_ranked = [('Diana', 95, 22), ('Bob', 92, 21), ('Eve', 88, 20),
                      ('Alice', 85, 20), ('Charlie', 78, 19)]
    print(f"\nStatus: {'✓ PASS' if ranked == expected_ranked else '✗ FAIL'}")
    print()

    # Test 3: Print numbered list
    print("TEST 3: Print numbered ranking using enumerate()")
    print("-" * 40)
    numbered = print_numbered_list(ranked)
    print("Result:")
    for line in numbered:
        print(f"  {line}")

    expected_format = [
        "1. Diana (age 22): 95 points",
        "2. Bob (age 21): 92 points",
        "3. Eve (age 20): 88 points",
        "4. Alice (age 20): 85 points",
        "5. Charlie (age 19): 78 points"
    ]
    print(f"\nStatus: {'✓ PASS' if numbered == expected_format else '✗ FAIL'}")
    print()

    # Bonus test
    print("=" * 60)
    print("BONUS TEST: Sort by age (youngest first)")
    print("=" * 60)
    by_age = sorted(records, key=lambda x: x[2])
    print("Students sorted by age:")
    for rank, student in enumerate(by_age, start=1):
        print(f"  {rank}. {student[0]} (age {student[2]}): {student[1]} points")
    print()
    print("=" * 60)


if __name__ == "__main__":
    test_student_ranker()
