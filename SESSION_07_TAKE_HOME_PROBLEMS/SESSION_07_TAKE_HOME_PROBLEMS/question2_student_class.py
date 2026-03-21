"""
SESSION 07 - Question 2: Student Class
Topics: Classes, __init__, methods, __str__, error handling

INSTRUCTIONS:
Complete the Student class below. Replace 'pass' with your code.
Run this file to test your implementation.
"""


class Student:
    """A class to represent a student with grades."""

    def __init__(self, name:str, age:int)-> None:
        """
        Initialize a new student.

        Args:
            name (str): Student's name
            age (int): Student's age

        Raises:
            ValueError: If age is negative or > 150
        """
        # TODO: Store name and age as attributes
        # TODO: Initialize empty grades list
        # TODO: Raise ValueError if age is invalid

        if age< 0 or age>150:
            raise ValueError("Age cannot be negative or below 150.")
        self.name:str = name
        self.age:int= age
        self.grades:list[float]=[]
        

    def add_grade(self, grade:float)-> None:
        """
        Add a grade to the student's grades list.

        Args:
            grade (int/float): The grade to add (0-100)

        Raises:
            ValueError: If grade is not between 0 and 100
            TypeError: If grade is not a number
        """
        # TODO: Validate that grade is a number (int or float)
        # TODO: Validate that grade is between 0 and 100
        # TODO: Append to self.grades if valid
        # TODO: Raise appropriate exceptions on error
        if not isinstance(grade,(int,float)):
            raise TypeError("Grade is a number")
        if grade< 0 or grade>100:
            raise ValueError("grae should be between 0 and 100.")
        self.grades.append(grade)

        

    def get_average(self)->float:
        """
        Calculate the average of all grades.

        Returns:
            float: Average grade, or 0 if no grades exist
        """
        # TODO: Return 0 if no grades
        # TODO: Otherwise return sum/count
        if not self.grades:
            return 0
        return sum(self.grades)/ len(self.grades)

    def get_letter_grade(self)->str:
        """
        Convert average to letter grade.

        Returns:
            str: Letter grade (A, B, C, D, or F)

        Grade scale:
            A: 90-100
            B: 80-89
            C: 70-79
            D: 60-69
            F: Below 60
        """
        # TODO: Get average using get_average()
        # TODO: Convert to letter grade and return
        avg= self.get_average()
        if avg>=90:
            return "A"
        elif avg>=80:
            return "B"
        elif avg>=80:
            return "C"
        elif avg>=80:
            return "D"
        else:
            return "F"

    def get_highest(self)-> float:
        """
        Get the highest grade.

        Returns:
            int/float: Highest grade, or 0 if no grades
        """
        # TODO: Return 0 if no grades
        # TODO: Otherwise return max(self.grades)
        if not self.grades:
            return 0
        return max(self.grades)

    def get_lowest(self):
        """
        Get the lowest grade.

        Returns:
            int/float: Lowest grade, or 0 if no grades
        """
        # TODO: Return 0 if no grades
        # TODO: Otherwise return min(self.grades)
        if not self.grades:
            return 0
        return min(self.grades)

    def __str__(self) -> str:
        """
        Return a string representation of the student.

        Returns:
            str: Formatted student info

        Example:
            "Student(Alice, Age 20, Avg: 85.0, Grade: B)"
        """
        # TODO: Create formatted string with:
        # - Name, Age
        # - Average (formatted to 1 decimal place)
        # - Letter grade
        avg = self.get_average()
        letter= self.get_letter_grade()
        return f"Student({self.name},Age{self.age},Avg:{avg:.1f},Grade:{letter})"


# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_student_class():
    """Test Student class"""
    print("="*60)
    print("TESTING STUDENT CLASS")
    print("="*60)

    # Test 1: Create student
    print("\n[Test 1] Creating student...")
    try:
        alice = Student("Alice", 20)
        print("✓ PASS: Student created successfully")
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return

    # Test 2: Add grades
    print("\n[Test 2] Adding grades...")
    try:
        alice.add_grade(85)
        alice.add_grade(92)
        alice.add_grade(78)
        print(f"✓ PASS: Added 3 grades: {alice.grades}")
    except Exception as e:
        print(f"✗ FAIL: {e}")

    # Test 3: Get average
    print("\n[Test 3] Getting average...")
    avg = alice.get_average()
    if abs(avg - 85.0) < 0.01:
        print(f"✓ PASS: Average = {avg}")
    else:
        print(f"✗ FAIL: Expected 85.0, got {avg}")

    # Test 4: Get letter grade
    print("\n[Test 4] Getting letter grade...")
    letter = alice.get_letter_grade()
    if letter == "B":
        print(f"✓ PASS: Letter grade = {letter}")
    else:
        print(f"✗ FAIL: Expected 'B', got {letter}")

    # Test 5: Get highest and lowest
    print("\n[Test 5] Getting highest and lowest...")
    highest = alice.get_highest()
    lowest = alice.get_lowest()
    if highest == 92 and lowest == 78:
        print(f"✓ PASS: Highest = {highest}, Lowest = {lowest}")
    else:
        print(f"✗ FAIL: Expected (92, 78), got ({highest}, {lowest})")

    # Test 6: String representation
    print("\n[Test 6] Testing __str__...")
    str_repr = str(alice)
    if "Alice" in str_repr and "85" in str_repr and "B" in str_repr:
        print(f"✓ PASS: {str_repr}")
    else:
        print(f"✗ FAIL: String representation incorrect: {str_repr}")

    # Test 7: Invalid grade (too high)
    print("\n[Test 7] Adding invalid grade (> 100)...")
    try:
        alice.add_grade(150)
        print("✗ FAIL: Should raise ValueError for grade > 100")
    except ValueError:
        print("✓ PASS: ValueError raised for grade > 100")

    # Test 8: Invalid grade (negative)
    print("\n[Test 8] Adding invalid grade (< 0)...")
    try:
        alice.add_grade(-10)
        print("✗ FAIL: Should raise ValueError for negative grade")
    except ValueError:
        print("✓ PASS: ValueError raised for negative grade")

    # Test 9: Empty student
    print("\n[Test 9] Testing student with no grades...")
    bob = Student("Bob", 21)
    if bob.get_average() == 0 and bob.get_highest() == 0:
        print("✓ PASS: Empty student returns 0 for average/highest")
    else:
        print("✗ FAIL: Empty student handling incorrect")

    # Test 10: Single grade
    print("\n[Test 10] Testing single grade...")
    charlie = Student("Charlie", 19)
    charlie.add_grade(95)
    if charlie.get_average() == 95 and charlie.get_letter_grade() == "A":
        print("✓ PASS: Single grade handled correctly (95 = A)")
    else:
        print(f"✗ FAIL: Single grade handling incorrect")

    print("\n" + "="*60)
    print("TESTS COMPLETE")
    print("="*60)


if __name__ == "__main__":
    test_student_class()
    print("\n💡 TIP: Implement all methods to pass all tests!")
    print("💡 TIP: Remember to use 'self' to access instance attributes!")
