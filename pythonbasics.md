What is programming : it it a process of writing instructions that a computer can understand and perform the tasks.
why we use programming to build apps,websites, games etc..
ex: a teacher giving step-by-step instructions to a student.

why python: Python code looks very close to regular language. You don’t need to write confusing symbols or lines.shorter, easier to understand.it has free libraries like pandas, matplotlib.

packages: it is a collection of modules (python files) that contain a prewritten code for specific tasks.we can reuse code which is written by experts we no need to start from the code from starting.
ex: each notebook is module.
    each school bag is a package.
popular packages are :
Package	                       Example
matplotlib	           Plot graphs of students' marks
pandas	               Manage tables like student records
numpy	               Math operations for scoring systems
openpyxl	           Read/write Excel sheets (marksheets)
sklearn	               AI predictions for student performance.

operators : Operators are special symbols or words that perform operations on values or variables.

1. Arthemetic : used to perform  basic math operations.
Operator	         Meaning	                   Example 	                      Output
+	                 Addition	           marks1 + marks2 (80 + 70)	           150
-	                 Subtraction	       total_marks - obtained_marks	100-80      20
*	                 Multiplication	       subject_count * 5 (4 * 5)	            20
/	                 Division	           total / 3 (210 / 3)	                   70.0
//	                 Floor Division	       215 // 3 (how many full sets of 3)	    71
%	                 Modulus	           215 % 3 (remainder after division)	    2
**	                 Exponent	           2 ** 3 (2 to the power of 3)	            8
2.Comparison (Relational) Operators : used to compare operators( yes/no and trur/false)

| Operator | Meaning          | Example        | Output |
| -------- | ---------------- | -------------- | ------ |
|   ==     | Equal to         |   marks == 100 | False  |
|   !=     | Not equal to     |   marks != 100 | True   |
|    >     | Greater than     |   marks > 50   | True   |
|   <      | Less than        |   marks < 50   | False  |
|   >=     | Greater or equal |   marks >= 90  | False  |
|    <=    | Less or equal    |   marks <= 80  | True   |

3.Logical operators : used for combining multiple conditions

| Operator | Meaning      | Example                          | Output |
| -------- | ------------ | -------------------------------- | ------ |
|  and     | Both True    |   attendance > 75 and marks > 60 | True   |
|  or      | At least one |   attendance > 75 or marks > 60  | True   |
|  not     | Reverses     |   not (marks > 60)`              | False  |

4.Assignment operators : used to assign values to variables.

| Operator | Meaning             | Example                          |
| -------- | ------------------- | -------------------------------- |
|   =      | Assign              |   marks = 85                     |
|   +=     | Add and assign      |   marks += 5 (marks = marks + 5) |
|    -=    | Subtract and assign |   marks -= 5                     |
|   *=     | Multiply and assign |   marks *= 2                     |
|    /=    | Divide and assign   |   marks /= 2                     |

5.Membership operators : used to test if a value is in list or not.

| Operator | Meaning        | Example                   | Output |
| -------- | -------------- | ------------------------- | ------ |
|  in      | Is present     | "Math" in subjects        | True   |
|  not in  | Is not present | "Dance" not in subjects   | True   |

flowcharts : A flowchart is a diagram that visually shows the steps or flow of a process or a program using symbols like arrows, rectangles, diamonds, and ovals.

Common Flowchart Symbols
Symbol	                         Meaning
Oval	                    Start/End
Rectangle	                Process (like input or calculation)
Diamond	                    Decision (yes/no, true/false)
Arrow	                    Direction of flow

Functions : it is a reusable block of code that performs a specific task when called.
why we use functions:
reusability write once use many times
breaks big programs into small parts
easy to understand and debug
no need to repeat same code again.

types in functions:
1.Built-in functions : we can use without defining them.
 
Function	         Use	              
print()	        Display output	
len()	        Count items in a list or string	
sum()	        Add numbers	
max()	        Find largest number	
type()	        Show data type

2.user-defined functions: we define it with "def".

Function definition	: When you write  "def function_name()"
Function call:When you actually run it like  "function_name()" (or) Executes the function with realvalues
Parameter:	Placeholder in function (or) Input values taken by the function 
Argument:Actual value passed 
Return:	Sends result back to where function was called (Or) Gives the result back to the program.

parameters and arguments

parameter: are names used in the function definition.
argument: are values you pass when calling the function.

ex : def average(m1, m2, m3):    # m1, m2, m3 = parameters
    return (m1 + m2 + m3) / 3

average(80, 90, 100)        # 80, 90, 100 = arguments

argument types :



Datatypes: A data type tells Python what kind of value a variable is storing — like a number, text, list, etc.

types:
1.int : stores whole numbers 
2.float : stores decimal values
3.string : stores sequence of characters 
4.Boolean : Stores only two possible values: True or False. Used for decision making.
5.List : Stores multiple items in a single variable.Can contain any data type and is changeable (mutable)
6.Tuple : Similar to a list, but it is immutable (cannot be changed after creation).
7.Dictionary : Stores data in key-value pairs.Used when you want to label each item.
8.Set : Stores a collection of unique, unordered items.No duplicates are allowed.

| Data Type | Definition                  | Education Example     |
| --------- | --------------------------- | --------------------- |
|  int      | Whole numbers               |  students = 45        |
|   float   | Decimal numbers             |  avg = 88.6           |
|   str     | Text or characters          |  "Math"               |
|   bool    | True or False               |  passed = True        |
|   list    | Ordered, changeable group   |  ["Math", "English"]  |
|   tuple   | Ordered, unchangeable group |  ("Spring", "Fall")   |
|   dict    | Key-value mapping           |  {"name": "Asha"}     |
|   set     | Unordered, unique group     |  {85, 90, 95}         |

LOOPS : A loop allows you to run a block of code multiple times — either a fixed number of times or until a condition is met.

for       | Fixed repetitions / list items        
while     | Repeat until condition is false       
break     | Exit loop early                 
continue  | Skip current loop and continue.


for loop : Used when you know how many times you want to repeat something.
while loop : Used when you don’t know in advance how many times to repeat.
             It repeats as long as a condition is true.
break : The break statement is used to exit a loop immediately, even if the loop condition is still true.
continue : The continue statement skips the current loop step and jumps to the next iteration.

conditional statements :

1.if: 




