datatypes in python
This module contains the datatypes used in the Genainotes application.
- int: Represents integer values.
- float: Represents floating-point numbers.
- str: Represents string values.
- bool: Represents boolean values (True or False).
- list: Represents a mutable sequence of values.
- tuple: Represents an immutable sequence of values.
- dict: Represents a collection of key-value pairs.
- set: Represents an unordered collection of unique values.


| Data Type | Definition                        | Real-Time Example             | Python Code Example              | Properties                                     |
| --------- | --------------------------------- | ----------------------------- | -------------------------------- | ---------------------------------------------- |
| `int`     | Whole numbers without decimals    | Number of students in a class | `students = 30`                  | ✅ Immutable<br>✅ Allows duplicates             |
| `float`   | Decimal numbers                   | Student's average marks       | `average = 85.6`                 | ✅ Immutable<br>✅ Allows duplicates             |
| `str`     | Sequence of characters (text)     | Student name or subject title | `name = "Asha"`                  | ✅ Immutable<br>✅ Allows duplicates             |
| `bool`    | Boolean values: `True` or `False` | Pass/fail status              | `is_passed = True`               | ✅ Immutable<br>✖ Not meaningful for duplicates |
| `list`    | Ordered, mutable collection       | Subjects taken by a student   | `subjects = ["Math", "Science"]` | ✅ Mutable<br>✅ Allows duplicates               |
| `tuple`   | Ordered, immutable collection     | Academic semesters            | `semesters = ("Spring", "Fall")` | ✅ Immutable<br>✅ Allows duplicates             |
| `dict`    | Key-value pairs                   | Student info with labels      | \`student = {"name": "R          |                                                |

tuple indexing:
a specific element in a tuple using its position number.
   Index starts at 0
   Negative indexes start from -1 (last item)
ex:subjects = ("Math", "Science", "English", "History")

print(subjects[0])   # Output: Math
print(subjects[2])   # Output: English
print(subjects[-1])  # Output: History


tuple slicing:
a specific range of elements in a tuple using slicing.
   Slicing allows you to extract a portion of the tuple.
   Syntax: tuple[start:end] where start is inclusive and end is exclusive
   includes start, excludes stop
   Optional: tuple[start:stop:step]
ex:subjects = ("Math", "Science", "English", "History", "Geography")

print(subjects[1:4])      # Output: ('Science', 'English', 'History')
print(subjects[:3])       # Output: ('Math', 'Science', 'English')
print(subjects[2:])       # Output: ('English', 'History', 'Geography')
print(subjects[::2])      # Output: ('Math', 'English', 'Geography')


list indexing:
a specific element in a list using its position number.
Index starts at 0
Negative indexes start from -1 (last item)
ex: print(subjects[0])   # Output: Math
print(subjects[2])   # Output: English
print(subjects[-1])  # Output: Geography (last item)
print(subjects[-3])  # Output: English

list slicing:
Slicing lets you access a sublist (a portion of the list).
Starts from start index
Stops before the stop index
ex:subjects = ["Math", "Science", "English", "History", "Geography"]

print(subjects[1:4])    # ['Science', 'English', 'History']
print(subjects[:3])     # ['Math', 'Science', 'English']
print(subjects[2:])     # ['English', 'History', 'Geography']
print(subjects[::2])    # ['Math', 'English', 'Geography'] (step = 2)
print(subjects[::-1])   # Reversed list

#Identifiers:
Identifiers are names used to identify variables, functions, classes, or other objects in Python.
   They must start with a letter (a-z, A-Z) or an underscore (_), followed by letters, digits (0-9), or underscores.
   Identifiers are case-sensitive, meaning 'myVariable' and 'myvariable' are different.
   Examples of valid identifiers: my_variable, _temp, student1
   Examples of invalid identifiers: 1st_student (starts with a digit), my-variable (contains hyphen)

#Intendation:
Indentation is the use of whitespace (spaces or tabs) at the beginning of a line to define the structure of code blocks in Python.
   It is used to indicate which statements belong to a particular block, such as loops, conditionals, and function definitions.
   Proper indentation is crucial in Python, as it determines the grouping of statements.
   Example:
   if condition:
       # This block is indented
       do_something()
   else:
       # This block is also indented
       do_something_else()


#Docstring : A string literal immediately after a function or class definition used as documentation.
ex:
def greet():
    """This function prints a greeting.""" //docstring//
    print("Hello!")

#String Indexing : access characters by index.
ex: text = "Python"
print(text[0])  # 'P'

#String Slicing: Extract a portion of string.
ex:print(text[:3])  # 'Pyt'

#string operations: 1.append a string
ex: name = "Py"
name += "thon"
print(name)  # Output: Python
explanation: "Py" is the starting value of the variable name.
The line name += "thon" adds "thon" to the end of "Py", making it "Python".
+= is a shorthand for: name = name + "thon"

2.Circulate Using Slicing
ex: take "python"
print(name[1:] + name[0])  # Output: ythonP
explanation: name = "Python" (from earlier)
name[1:] → This slices the string from index 1 to the end, which gives: "ython"
name[0] → This gets the first character, which is: "p"
then it adds up : "ython" + "P" → "ythonP"

#Sorting: Arrange items in order.
ex:marks = [90, 85, 95]
marks.sort()
print(marks)  # [85, 90, 95]

