"""
SESSION 05 - QUESTION 4: DATA STRUCTURES (Tuples & Sets)
=========================================================

Topics Covered: Tuples (immutable), Sets (unique items, set operations)

TASK:
Complete the five functions below to work with tuples and sets.
All the printing and formatting is handled for you - just implement the logic!

DO NOT modify the test code at the bottom.
"""

def create_coordinate(x, y):
   return(x,y)


def unpack_person(person_tuple):
   
   name,age,city = person_tuple

   return(name,age,city)


def remove_duplicates(items):
 return list(set(items))


def find_common_items(list1, list2):
  return set(list1) & set(list2)




def find_unique_items(list1, list2):
    return set(list1)- set(list2)


# ============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# ============================================================================

def test_data_structures():
    """Test function with formatted output"""
    print("=" * 60)
    print("SESSION 05 - QUESTION 4: DATA STRUCTURES")
    print("=" * 60)
    print()

    # Test 1: Create coordinate tuple
    print("TEST 1: Create a coordinate tuple")
    print("-" * 40)
    coord = create_coordinate(10, 20)
    print(f"Result: {coord}")
    print(f"Expected: (10, 20)")
    print(f"Status: {'✓ PASS' if coord == (10, 20) else '✗ FAIL'}")
    print()

    # Test 2: Unpack person tuple
    print("TEST 2: Unpack a person tuple")
    print("-" * 40)
    person = ("Alice", 25, "New York")
    name, age, city = unpack_person(person)
    print(f"Input: {person}")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Status: {'✓ PASS' if (name, age, city) == ('Alice', 25, 'New York') else '✗ FAIL'}")
    print()

    # Test 3: Remove duplicates
    print("TEST 3: Remove duplicates using set")
    print("-" * 40)
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
    unique = remove_duplicates(numbers)
    unique_sorted = sorted(unique)  # Sort for consistent comparison
    print(f"Input: {numbers}")
    print(f"Result: {unique_sorted}")
    print(f"Expected: [1, 2, 3, 4, 5]")
    print(f"Status: {'✓ PASS' if unique_sorted == [1, 2, 3, 4, 5] else '✗ FAIL'}")
    print()

    # Test 4: Find common items (intersection)
    print("TEST 4: Find common items (intersection)")
    print("-" * 40)
    alice_courses = ["Math", "Physics", "Chemistry", "Biology"]
    bob_courses = ["Physics", "Chemistry", "History", "Art"]
    common = find_common_items(alice_courses, bob_courses)
    print(f"Alice's courses: {alice_courses}")
    print(f"Bob's courses: {bob_courses}")
    print(f"Common courses: {common}")
    print(f"Expected: {{'Physics', 'Chemistry'}}")
    print(f"Status: {'✓ PASS' if common == {'Physics', 'Chemistry'} else '✗ FAIL'}")
    print()

    # Test 5: Find unique items (difference)
    print("TEST 5: Find unique items (difference)")
    print("-" * 40)
    alice_only = find_unique_items(alice_courses, bob_courses)
    print(f"Alice's courses: {alice_courses}")
    print(f"Bob's courses: {bob_courses}")
    print(f"Courses only Alice takes: {alice_only}")
    print(f"Expected: {{'Math', 'Biology'}}")
    print(f"Status: {'✓ PASS' if alice_only == {'Math', 'Biology'} else '✗ FAIL'}")
    print()

    # Bonus demonstration
    print("=" * 60)
    print("BONUS: More set operations")
    print("=" * 60)
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union (all items): {set1 | set2}")
    print(f"Intersection (common): {set1 & set2}")
    print(f"Difference (in set1 only): {set1 - set2}")
    print(f"Symmetric difference (in either, not both): {set1 ^ set2}")
    print()
    print("=" * 60)


if __name__ == "__main__":
    test_data_structures()
