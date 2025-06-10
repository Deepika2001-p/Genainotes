""" function : a function is a block of code (or) 
a set of instructions that performs a specific task when it is called.
It can take inputs, process them, and return outputs.
"""
"""# Example of a simple function in Python"""
def greet(name):
    print(f"hello {name}")
    print("how are you?")
greet("Deepika")  
greet("Pravallika")

"""types of functions in Python:
1. Built-in functions: These are functions that are already defined in Python, such as `print()`, `len()`, and `type()`.
2. User-defined functions: These are functions that you define yourself to perform specific tasks. 
You can create a user-defined function using the `def` keyword, followed by the function name and parentheses.
3. Lambda functions: These are small anonymous functions defined using the `lambda` keyword. 
They can take any number of arguments but can only have one expression."""


"""# Example of a user-defined function"""
def add(a, b):
    return a + b
result = add(5, 3)
print(f"The sum is: {result}")


"""# Example of a lambda function"""
multiply = lambda x, y: x * y #This is a lambda function that takes two arguments and returns their product
result = multiply(4, 5)
print(f"The product is: {result}")

"""# Example of a function with default parameters"""
def greet(name="Family"):
    print(f"Hello {name}!")
greet()  # Calls the function with the default parameter
greet("Deepika")  # Calls the function with a specific name

"""# Example of a function with variable-length arguments"""
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1, 2, 3)  # Calls the function with three arguments
def print_all(*args):
    for arg in args:
        print(arg)
print_all("apple", "banana", "cherry")  # Calls the function with three string arguments


"""# Example of a function with keyword arguments"""
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")
print_info(name="Deepika", age=24)  # Calls the function with keyword arguments
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")
print_info(age=24, name="Deepika")  # Calls the function with keyword arguments in a different order


"""# Example of a function with a return value"""
def square(x):
    return x * x
result = square(5)
print(f"The square of 5 is: {result}")  # Prints the result of the function call

"""# Example of a function that returns multiple values"""
def get_info():
    name = "Deepika"
    age = 24
    return name, age
name, age = get_info()
print(f"Name: {name}, Age: {age}")  # Prints the returned values from the function

"""what is recursion function: A recursion function is a function that calls itself in order to solve a problem.
# Example of a recursive function"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
result = factorial(5)
print(f"The factorial of 5 is: {result}")  # Prints the result of the recursive function call

"""what is a docstring: A docstring is a special type of comment in Python that is used to describe 
                        the purpose and behavior of a function, class, or module.
# Example of a function with a docstring"""
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b
print(add(3, 4))  # Calls the function and prints the result
def multiply(a, b):
    """This function returns the product of two numbers."""
    return a * b
print(multiply(3, 4))  # Calls the function and prints the result


"""
what is type hinting: Type hinting is a feature in Python that allows you to specify 
                      the expected data types of function parameters and return values.
# Example of a function with type hints"""

def divide(a: float, b: float) -> float:
    """This function returns the result of dividing a by b."""
    return a / b
result = divide(10.0, 2.0)
print(f"The result of division is: {result}")  # Prints the result of the function call
def concatenate_strings(str1: str, str2: str) -> str:
    """This function returns the concatenation of two strings."""
    return str1 + str2
result = concatenate_strings("Hello, ", "World")
print(f"The concatenated string is: {result}")  # Prints the result of the function call
"""# Example of a function with a nested function"""
def outer_function(x):
    """This function contains a nested function that squares the input."""
    def inner_function(y):
        return y * y
    return inner_function(x)
result = outer_function(5)
print(f"The result of the outer function is: {result}")  # Prints the result of the outer function call
def outer_function(x):
    """This function contains a nested function that adds 10 to the input."""
    def inner_function(y):
        return y + 10
    return inner_function(x)
result = outer_function(5)
print(f"The result of the outer function is: {result}")  # Prints the result of the outer function call

#types of arguments.
"""types of arguments in Python:
1. Positional arguments: These are the most common type of arguments, 
                         where the values are passed to the function in the order they are defined.
2. Keyword arguments: These are arguments that are passed to the function by explicitly specifying the parameter name and value.
3. Default arguments: These are arguments that have a default value specified in the function definition.
4. Variable-length arguments: These allow you to pass a variable number of arguments to a function 
                              using the `*args` syntax for non-keyword arguments and `**kwargs` for keyword arguments.
5. Keyword-only arguments: These are arguments that must be passed using their keyword name, 
                            and they come after a `*` in the function definition."""




"""# Example of a function with positional arguments"""
def add(a, b):
    #This function returns the sum of two numbers.
    return a + b
result = add(3, 4)  # Calls the function with positional arguments
print(f"The sum is: {result}")  # Prints the result of the function call

"""# Example of a function with keyword arguments"""
def print_info(name, age):
     #This function prints the name and age of a person.
    print(f"Name: {name}, Age: {age}")
print_info(name="Deepika", age=24)  # Calls the function with keyword arguments
def print_info(age, name):
    """This function prints the age and name of a person."""
    print(f"Age: {age}, Name: {name}")
print_info(age=24, name="Deepika")  # Calls the function with keyword arguments in a different order


"""# Example of a function with default arguments"""
def greet(name="Family"):
    """This function greets a person with a default name."""
    print(f"Hello {name}!")
greet()  # Calls the function with the default parameter
greet("Deepika")  # Calls the function with a specific name

"""# Example of a function with variable-length arguments"""
def print_numbers(*args):
    """This function prints a variable number of arguments."""
    for number in args:
        print(number)
print_numbers(1, 2, 3)  # Calls the function with three arguments
def print_all(*args):
    """This function prints all the arguments passed to it."""
    for arg in args:
        print(arg)
print_all("apple", "banana", "cherry")  # Calls the function with three string arguments


"""# Example of a function with keyword arguments"""
def print_info(name, age):
    """This function prints the name and age of a person."""
    print(f"Name: {name}, Age: {age}")
print_info(name="Deepika", age=24)  # Calls the function with keyword arguments
def print_info(age, name):
    """This function prints the age and name of a person."""
    print(f"Age: {age}, Name: {name}")
print_info(age=24, name="Deepika")  # Calls the function with keyword arguments in a different order



