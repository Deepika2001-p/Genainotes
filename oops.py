"""This code demonstrates the principles of Object-Oriented Programming (OOP) in Python
by implementing a simple education portal system. It showcases the four main OOP concepts: Abstraction, Encapsulation, Inheritance, and Polymorphism.
"""


"""
This code demonstrates Object-Oriented Programming (OOP) concepts in Python
through an Education Portal system with Students and Teachers.
"""

from abc import ABC, abstractmethod

# Abstraction using Abstract Base Class
class EducationPortal(ABC):
    @abstractmethod
    def access_portal(self):
        pass

# Base class
class Person:
    def __init__(self, name, person_id):
        self.name = name
        self.person_id = person_id

# Student class (inherits Person, implements EducationPortal)
class Student(Person, EducationPortal):
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.__grades = {}  # Encapsulated

    def add_grade(self, subject, grade):
        self.__grades[subject] = grade

    def view_grades(self):
        print(f"\nGrades for {self.name}:")
        for subject, grade in self.__grades.items():
            print(f"  {subject}: {grade}")

    def access_portal(self):  # Polymorphism
        print(f"Student {self.name} is accessing the student portal.")

# Teacher class (inherits Person, implements EducationPortal)
class Teacher(Person, EducationPortal):
    def __init__(self, name, teacher_id, subject):
        super().__init__(name, teacher_id)
        self.subject = subject

    def assign_grade(self, student, grade):
        student.add_grade(self.subject, grade)

    def access_portal(self):  # Polymorphism
        print(f"Teacher {self.name} is accessing the teaching portal.")

# List of students
students = [
    Student("Deepika", 101),
    Student("Meghana", 102),
    Student("Rajesh", 103),
    Student("Rekha", 104),
    Student("Pravallika", 105),
    Student("Renuka", 106),
    Student("Akshaya", 107),
    Student("Sai", 108),
    Student("Latha", 109),
    Student("Divya", 110),
    Student("Kavya", 111),
    Student("Alekhya", 112),
    Student("Gayathri", 113),
    Student("Prasanna", 114),
]

# Teachers for different subjects
math_teacher = Teacher("Mr. Srinivasrao", 201, "Math")
science_teacher = Teacher("Ms. Anuradha", 202, "Science")
english_teacher = Teacher("Mrs. Neelima", 203, "English")

# Sample grades to assign
grades = {
    "Math": [90, 85, 78, 92, 88, 74, 91, 80, 86, 79, 83, 87, 89, 84],
    "Science": [88, 80, 76, 90, 85, 70, 95, 82, 89, 77, 81, 86, 90, 83],
    "English": [92, 87, 75, 94, 90, 79, 88, 85, 91, 76, 80, 84, 89, 82]
}

# Assign grades to all students in all subjects
for i, student in enumerate(students):
    math_teacher.assign_grade(student, grades["Math"][i])
    science_teacher.assign_grade(student, grades["Science"][i])
    english_teacher.assign_grade(student, grades["English"][i])

# Demonstrate access_portal (Polymorphism)
math_teacher.access_portal()
science_teacher.access_portal()
english_teacher.access_portal()

# Student portal access and viewing grades
for student in students:
    student.access_portal()
    student.view_grades()




