"""
File main.py
-the user interface for the Student class.
This function tests the methods in the class.
"""
from student import Student


def main():
    # construct a Student object with name Aaron, and space for 5 test scores
    student1 = Student("Aaron", 5)
    print("Initialized student: ", student1)
    print("")

    # set the scores for each test
    student1.setScore(1, 100)
    student1.setScore(2, 89)
    student1.setScore(3, 95)
    student1.setScore(4, 72)
    student1.setScore(5, 85)

    # printing the student1 object displays a string representation of the object
    # Same as calling student1.__str__()
    print("Student with test scores: ", student1)
    print("")

    # Test the rest of the accessor functions in the Student class
    print("Test summary for ", student1.getName(), ":")
    print("High score: ", student1.getHighScore())
    print("Average score: ", student1.getAverage())
    print("Third test score: ", student1.getScore(3))

    # ~ Jace's code ~
    # Test the operator overload functions

    # initialize second student
    student2 = Student("Jace", 5)
    print("Initialized student: ", student2)
    print("")

    # set the scores for each test
    student2.setScore(1, 95)
    student2.setScore(2, 98)
    student2.setScore(3, 79)
    student2.setScore(4, 82)
    student2.setScore(5, 100)
    student2.__str__()

    print("less than: " + str(student1.__lt__(student2)))
    print("less than or equal to: " + str(student1.__le__(student2)))
    print("greater than: " + str(student1.__gt__(student2)))
    print("greater than or equal to: " + str(student1.__ge__(student2)))
    print("equal to: " + str(student1.__eq__(student2)))


main()
