"""
SESSION 07 - Question 4: Classroom Manager
Topics: Multiple classes, composition, @property, file I/O, error handling

INSTRUCTIONS:
Complete the Classroom class below (uses Student from question2_student_class.py).
Replace 'pass' with your code.
Run this file to test your implementation.

NOTE: This question uses the Student class from question2_student_class.py
You'll need to import it or have it in the same file.
"""

from question2_student_class import Student

# First, copy the Student class here or import it
# For this exercise, we'll define it inline:

class Student:
    """A class to represent a student with grades."""

    def __init__(self, name:str, age:int)-> None:
        if age < 0 or age > 150:
            raise ValueError("Age must be between 0 and 150!")
        self.name = name
        self.age = age
        self.grades: list[float]= []

    def add_grade(self, grade:float)-> None:
        if not isinstance(grade, (int, float)):
            raise TypeError("Grade must be a number!")
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100!")
        self.grades.append(grade)

    def get_average(self)-> float:
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_letter_grade(self)->str:
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def get_highest(self)->float:
        return max(self.grades) if self.grades else 0

    def get_lowest(self)->float:
        return min(self.grades) if self.grades else 0

    def __str__(self)->float:
        avg = self.get_average()
        return f"Student({self.name}, Age {self.age}, Avg: {avg:.1f}, Grade: {self.get_letter_grade()})"


# NOW implement the Classroom class

class Classroom:
    """A class to represent a classroom with multiple students."""

    def __init__(self, name:str)->None:
        """
        Initialize a new classroom.

        Args:
            name (str): Name of the classroom
        """
        # TODO: Store classroom name
        # TODO: Initialize empty list of students: self.students = []
        self.name:str = name
        self.students: list[Student]=[]

    def add_student(self, student:Student)->None:
        """
        Add a student to the classroom.

        Args:
            student (Student): Student object to add

        Raises:
            ValueError: If a student with that name already exists
        """
        # TODO: Check if student name already in classroom (raise ValueError if so)
        # TODO: Append student to self.students if not duplicate
        for stud in self.students:
            if stud.name == student.name:
                raise ValueError("student name already in classroom")
        self.students.append(student)

    def remove_student(self, name:str) -> None:
        """
        Remove a student from the classroom by name.

        Args:
            name (str): Name of the student to remove

        Raises:
            ValueError: If student not found
        """
        # TODO: Find student by name and remove from self.students
        # TODO: Raise ValueError if student not found
        student = self.get_student(name)
        if student is None:
            raise ValueError("Student not found")
        self.students.remove(student)

    def get_student(self, name:str):
        """
        Find and return a student by name.

        Args:
            name (str): Name of the student to find

        Returns:
            Student: The student object, or None if not found
        """
        # TODO: Loop through self.students and return student with matching name
        # TODO: Return None if not found
        for student in self.students:
            if student.name== name:
                return student
        return None

    @property
    def class_average(self)-> float:
        """
        Get the class-wide average grade.

        Returns:
            float: Average of all students' averages, or 0 if no students
        """
        # TODO: Calculate average of all students' get_average() values
        # TODO: Return 0 if no students
        if not self.students:
            return 0
        total = sum(student.get_average() for student in self.students)
        return total/len(self.students)

    @property
    def top_student(self):
        """
        Get the highest-performing student.

        Returns:
            Student: Student with highest average, or None if no students
        """
        # TODO: Use max() with key=lambda to find student with highest average
        # TODO: Return None if no students
        if not self.students:
            return None
        return max(self.students,key=lambda s: s.get_average())
        

    def get_honor_roll(self)-> list[Student]:
        """
        Get all students with average >= 90.

        Returns:
            list: List of Student objects on honor roll
        """
        # TODO: Use list comprehension to filter students with average >= 90
        return [student for student in self.students if student.get_average()>=90]

    def save_to_file(self, filename:str)->None:
        """
        Save classroom data to a CSV file.

        Args:
            filename (str): Name of file to save to

        CSV Format:
            name,age,grades,average,letter_grade
            Alice,20,95;88;92,91.7,A
            Bob,21,75;82;78,78.3,C
        """
        # TODO: Open file in write mode
        # TODO: Write header: "name,age,grades,average,letter_grade"
        # TODO: For each student, write:
        #      - name, age
        #      - grades joined with semicolons: ";".join(map(str, grades))
        #      - average (formatted to 1 decimal place)
        #      - letter grade
        with open(filename,"w") as f:
            f.write("name,age,grades,average,letter_grade\n")
            for studint in self.students:
                grades_str = ";".join(map(str, studint.grades))
                avg = studint.get_average()
                letter = studint.get_letter_grade()
                f.write(f"{studint.name},{studint.age},{grades_str},{avg:.1f},{letter}\n")

    def __str__(self)-> str:
        """
        Return a string representation of the classroom.

        Returns:
            str: Formatted classroom info

        Example:
            "Classroom(Python 101, 2 students, Avg: 85.0)"
        """
        # TODO: Create formatted string with:
        # - Classroom name
        # - Number of students
        # - Class average (formatted to 1 decimal place)
        # TODO: Format: "Classroom({name}, {count} students, Avg: {avg:.1f})"
        count = len(self.students)
        avg = self.class_average
        return f"Classroom({self.name}, {count} students, Avg: {avg:.1f})"


# =============================================================================
# TEST CODE - DO NOT MODIFY BELOW THIS LINE
# =============================================================================

def test_classroom():
    """Test Classroom class"""
    print("="*60)
    print("TESTING CLASSROOM CLASS")
    print("="*60)

    # Test 1: Create classroom
    print("\n[Test 1] Creating classroom...")
    try:
        classroom = Classroom("Python 101")
        print("✓ PASS: Classroom created successfully")
    except Exception as e:
        print(f"✗ FAIL: {e}")
        return

    # Test 2: Create and add students
    print("\n[Test 2] Adding students...")
    try:
        alice = Student("Alice", 20)
        alice.add_grade(95)
        alice.add_grade(88)
        alice.add_grade(92)

        bob = Student("Bob", 21)
        bob.add_grade(75)
        bob.add_grade(82)
        bob.add_grade(78)

        classroom.add_student(alice)
        classroom.add_student(bob)
        print("✓ PASS: 2 students added")
    except Exception as e:
        print(f"✗ FAIL: {e}")

    # Test 3: Class average
    print("\n[Test 3] Checking class average...")
    class_avg = classroom.class_average
    # expected =(91.666... + 78.333...) / 2
    if abs(class_avg - 85.0) < 1:  # Rough check
        print(f"✓ PASS: Class average = {class_avg:.1f}")
    else:
        print(f"✗ FAIL: Class average incorrect: {class_avg:.1f}")

    # Test 4: Top student
    print("\n[Test 4] Checking top student...")
    top = classroom.top_student
    if top and top.name == "Alice":
        print(f"✓ PASS: Top student = {top.name}")
    else:
        print(f"✗ FAIL: Expected Alice, got {top.name if top else None}")

    # Test 5: Honor roll
    print("\n[Test 5] Checking honor roll...")
    honor_roll = classroom.get_honor_roll()
    if len(honor_roll) == 1 and honor_roll[0].name == "Alice":
        print(f"✓ PASS: Honor roll has 1 student: {honor_roll[0].name}")
    else:
        print(f"✗ FAIL: Honor roll incorrect")

    # Test 6: String representation
    print("\n[Test 6] Testing __str__...")
    str_repr = str(classroom)
    if "Python 101" in str_repr and "2 students" in str_repr:
        print(f"✓ PASS: {str_repr}")
    else:
        print(f"✗ FAIL: String representation incorrect: {str_repr}")

    # Test 7: Get student
    print("\n[Test 7] Getting student by name...")
    student = classroom.get_student("Alice")
    if student and student.name == "Alice":
        print(f"✓ PASS: Found student: {student.name}")
    else:
        print(f"✗ FAIL: Could not find Alice")

    # Test 8: Duplicate student
    print("\n[Test 8] Trying to add duplicate student...")
    try:
        duplicate_alice = Student("Alice", 22)
        classroom.add_student(duplicate_alice)
        print("✗ FAIL: Should raise ValueError for duplicate name")
    except ValueError:
        print("✓ PASS: ValueError raised for duplicate name")

    # Test 9: Save to file
    print("\n[Test 9] Saving classroom to file...")
    try:
        classroom.save_to_file("test_classroom.csv")
        # Check if file was created
        import os
        if os.path.exists("test_classroom.csv"):
            print("✓ PASS: File created successfully")
            # Check contents
            with open("test_classroom.csv", "r") as f:
                contents = f.read()
                if "Alice" in contents and "Bob" in contents:
                    print("✓ PASS: File contains student data")
                else:
                    print("✗ FAIL: File data incorrect")
            os.remove("test_classroom.csv")
        else:
            print("✗ FAIL: File not created")
    except Exception as e:
        print(f"✗ FAIL: {e}")

    # Test 10: Remove student
    print("\n[Test 10] Removing student...")
    try:
        classroom.remove_student("Bob")
        if classroom.get_student("Bob") is None:
            print("✓ PASS: Student removed successfully")
        else:
            print("✗ FAIL: Student not removed")
    except Exception as e:
        print(f"✗ FAIL: {e}")

    print("\n" + "="*60)
    print("TESTS COMPLETE")
    print("="*60)


if __name__ == "__main__":
    test_classroom()
    print("\n💡 TIP: Implement all methods to pass all tests!")
    print("💡 TIP: Use @property for class_average and top_student!")
    print("💡 TIP: Use list comprehension for get_honor_roll!")
