File handling : File handling is the process of creating, opening, reading, writing, and updating files using a programming language. In Python, file handling is done using built-in functions like open(), read(), write(), and close().

basic handling operators :
| Operation | Method                                | Purpose                 |
| --------- | ------------------------------------- | ----------------------- |
| Open      | `open()`                              | Opens a file            |
| Read      | `read()`, `readline()`, `readlines()` | Reads content from file |
| Write     | `write()`, `writelines()`             | Writes content to file  |
| Close     | `close()`                             | Closes the file         |

Open modes :

| Mode   | Meaning                    | Behavior                                             |
| ------ | -------------------------- | ---------------------------------------------------- |
|   'r'  | Read                       | Opens file for reading (error if file not found)     |
|  'w'   | Write                      | Creates file if not exists, "overwrites" if exists |
|   'a'  | Append                     | Adds content to the end of the file                  |
|  'r+'  | Read and Write             | Can both read and write                              |
|  'w+'  | Write and Read (overwrite) | Same as `w`, but allows reading                      |

benefits of file handling : Store data permanently (unlike variables which are temporary)
                            Save user input or program output
                            Read data from files like CSV, TXT, logs
                            Log errors or events (e.g., system logs, audit trails)

Exception handling : is a mechanism that allows your program to gracefully respond to errors during runtime, instead of crashing.

benefits of using : To avoid program crashes
                    To handle unexpected input or events
                    To show meaningful error messages to the user
common errors: 
             ZeroDivisionError : When dividing a number by zero       
             FileNotFoundError : When trying to open a file that doesn't exist       
             typeError : When incompatible types are used (e.g. adding string to int)
             valueError: When wrong data type is given (e.g. text instead of number)

| Keyword   | Purpose                                             |
| --------- | --------------------------------------------------- |
| `try`     | Block of code to test for errors                    |
| `except`  | Block that runs if an error occurs                  |
| `else`    | Runs if there is **no error**                       |
| `finally` | Always runs — used for cleanup (like closing files) |

example :
try: You try to swipe your card at an ATM
except: If card is declined, it gives you a message
else: If successful, it shows your balance
finally: Whether success or error, it returns your card

file.seek(0)  # Move the cursor to the beginning of the file

| Mode  | Description                          | Behavior                                                                 |
|-------|--------------------------------------|--------------------------------------------------------------------------|
| r     | Read-only mode                       | Opens the file for reading. File must exist; otherwise, it raises an error. |
| rb    | Read-only in binary mode             | Opens the file for reading binary data. File must exist; otherwise, it raises an error. |
| r+    | Read and write mode                  | Opens the file for both reading and writing. File must exist; otherwise, it raises an error. |
| rb+   | Read and write in binary mode        | Opens the file for both reading and writing binary data. File must exist; otherwise, it raises an error. |
| w     | Write mode                           | Opens the file for writing. Creates a new file or truncates the existing file. |
| wb    | Write in binary mode                 | Opens the file for writing binary data. Creates a new file or truncates the existing file. |
| w+    | Write and read mode                  | Opens the file for both writing and reading. Creates a new file or truncates the existing file. |
| wb+   | Write and read in binary mode        | Opens the file for both writing and reading binary data. Creates a new file or truncates the existing file. |
| a     | Append mode                          | Opens the file for appending data. Creates a new file if it doesn't exist. |
| ab    | Append in binary mode                | Opens the file for appending binary data. Creates a new file if it doesn't exist. |
| a+    | Append and read mode                 | Opens the file for appending and reading. Creates a new file if it doesn't exist. |
| ab+   | Append and read in binary mode       | Opens the file for appending and reading binary data. Creates a new file if it doesn't exist. |
| x     | Exclusive creation mode              | Creates a new file. Raises an error if the file already exists.          |
| xb    | Exclusive creation in binary mode    | Creates a new binary file. Raises an error if the file already exists.  |
| x+    | Exclusive creation with read/write   | Creates a new file for reading and writing. Raises an error if the file exists. |
| xb+   | Exclusive creation with read/write in binary | Creates a new binary file for reading and writing. Raises an error if the file exists. |




OOPS CONCEPTS : 
                   

OOPs Concepts Summary

| Concept        | Definition                                         | Real-World Use Case                                  |
|----------------|----------------------------------------------------|------------------------------------------------------|
| Encapsulation  | Hides internal data using methods                  | Protecting marks, passwords, banking systems         |
| Abstraction    | Shows only essential features                      | ATM, APIs, buttons hide internal logic               |
| Inheritance    | Child class inherits from parent class             | Developer inherits from Employee, Vehicle from Car   |
| Polymorphism   | Same method acts differently across classes        | area() in Circle vs Square                           |
| Class          | Blueprint for creating objects                     | class Student:                                       |
| Object         | Instance of a class                                | s1 = Student("Asha")                                 |
| Method         | Function inside a class                            | get_marks(), greet()                                 |
| Constructor    | __init__ runs when object is created               | Automatically set name, age                          |
| Destructor     | __del__ runs when object is deleted                | Cleanup: close files, release memory                 |




constructor : A constructor is a special method in Python called __init__() that automatically runs when an object is created. It’s used to initialize values (set up data) for the object.

ex: When you buy a phone → the company installs basic apps & settings → that’s like a constructor.


Destructor : A destructor is a special method called __del__() that automatically runs when an object is destroyed or deleted. It’s used to clean up resources like files, memory, or connections.
 ex:When you shut down your computer → it closes all apps → that’s like a destructor.