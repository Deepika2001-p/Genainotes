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

OOPS CONCEPTS : 
                   
| Concept          | Definition                                               | Real-World Use Case                                    |
+------------------+---------------------------------------------------------+------------------------------------------------------------+
| Encapsulation    | Hiding internal data and controlling access via methods  | Protecting marks, passwords, banking details               |
| Abstraction      | Showing only essential features, hiding the background   | ATM interface, APIs, app buttons hide internal logic       |
| Inheritance      | One class (child) inherits from another (parent)         | Developer inherits from Employee, Car from Vehicle         |
| Polymorphism     | Same method behaves differently in different classes     | `area()` for Circle vs Rectangle, `play()` for media types |
| Class            | Blueprint for creating objects                           | `class Student:` defines structure                         |
| Object           | Instance of a class with actual data                     | `s1 = Student("Asha")`                                     |
| Method           | Function inside a class operating on data                | `get_marks()`, `calculate_salary()`                        |
| Constructor      | `__init__` – runs when object is created                 | Initialize name, ID, etc. automatically                    |
| Destructor       | `__del__` – runs when object is deleted                  | Cleanup: closing files, freeing memory                     |
+------------------+----------------------------------------------------------+----------------------------------------------------------+

constructor : A constructor is a special method in Python called __init__() that automatically runs when an object is created. It’s used to initialize values (set up data) for the object.

ex: When you buy a phone → the company installs basic apps & settings → that’s like a constructor.


Destructor : A destructor is a special method called __del__() that automatically runs when an object is destroyed or deleted. It’s used to clean up resources like files, memory, or connections.
 ex:When you shut down your computer → it closes all apps → that’s like a destructor.