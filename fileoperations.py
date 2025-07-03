"""file handling and oops concepts:

1. File handling: Reading and writing files, handling exceptions.
2. Object-Oriented Programming (OOP): Classes, objects, inheritance, encapsulation, and polymorphism.
# 3. Exception handling: Using try-except blocks to handle errors gracefully.
# 4. Context managers: Using the `with` statement to manage resources like files.
# 5. File modes: Understanding different file modes like read ('r'), write ('w'), append ('a'), and binary ('b').
# 6. File operations: Opening, closing, reading, writing, and appending to files.
"""
"""examples of file operations : 
1. Reading a file: Using the `open()` function to read the contents of a file.
code:"""
with open('oops.txt', 'w') as file:
    file.write("this is my first file \n")
    file.write("includes code \n")

with open('oops.txt','r') as file:
    content = file.read()
    print(content)
"""2. Writing to a file: Using the `open()` function with 'w' mode to write data to a file."""
file= open('one.txt', 'w')
file.write("i want to close the file \n")
file.close()

file= open('one.txt', 'r') 
content = file.read()
print(content)

"""3. Appending to a file: Using the `open()` function with 'a' mode to add data to an existing file."""
file = open('one.txt', 'a')
file.write("This is an appended line one.")
file.close()
file = open('one.txt', 'r')
content = file.read()
print(content)

"""4. Reading a file line by line: Using a loop to read each line of a file.""" 
with open('oops.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Using strip() to remove leading/trailing whitespace

#using the line strip
# First, write to the file
with open('oops.txt', 'w') as file:
    file.write("this is my first file \n")
    file.write("this is my first file \n")
    file.write("this is my first file \n")
    file.write("")
    file.write("includes code \n")

# Then, read from the file
with open('oops.txt', 'r') as file:
    for line in file:
        print(line.strip())

# creating with r+ 
# mode to read and write to a file
with open('oops.txt', 'r+') as file:
    content = file.read()
    print("Current content of the file:")
    print(content)
    file.write("\nThis is an additional line added using r+ mode.")
# Now, let's read the file again to see the changes
with open('oops.txt', 'r') as file:
    updated_content = file.read()
    print("\nUpdated content of the file:")
    print(updated_content)

# creating with w+
# mode to write and read a file
with open('oops_w_plus.txt', 'w+') as file:
    file.write("This is a new file created with w+ mode.\n")
    file.write("It allows both writing and reading.\n")
    file.seek(0)  # Move the cursor back to the beginning of the file
    content = file.read()
    print("Content of the file after writing:")
    print(content)
# creating with a+
# mode to append and read a file
with open('oops_a_plus.txt', 'a+') as file:
    file.write("This line is appended to the file using a+ mode.\n")
    file.seek(0)  # Move the cursor back to the beginning of the file
    content = file.read()
    print("Content of the file after appending:")
    print(content)

# handling exceptions in file operations
try:
    with open('oops.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")

# using the try-except block to handle exceptions 
try:
    with open('oops.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")


#using finally and else in file operations
try:
    with open('oops.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")

#more 
try:
    x = int("42")
except ValueError:
    print("Invalid number!")
else:
    print("Conversion successful:", x) #output: Conversion successful: 42

#
try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("You didn't enter a number!")
except ZeroDivisionError:
    print("You can't divide by zero!") #output: You can't divide by zero!



#creating .csv file operations
import csv
# Writing to a CSV file 
data = [
    ["Name", "Age", "City"],
    ["Deepika", 24, "Delhi"],
    ["Rahul", 30, "Mumbai"],
    ["Anjali", 22, "Bangalore"]
]
with open('data.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)
# Reading from a CSV file
with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

# creating csv file reading
import csv
# Reading a CSV file and printing each row
with open('data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

#creating csv file appending
import csv
# Appending to a CSV file
data_to_append = [
    ["Sita", 28, "Chennai"],
    ["Ravi", 26, "Kolkata"]
]
with open('data.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data_to_append)

# creating csv file r+
import csv
# Reading and writing to a CSV file using r+ mode
with open('data.csv', 'r+', newline='') as csv_file:
    reader = csv.reader(csv_file)
    # Read existing data
    existing_data = list(reader)
    print("Existing data:")
    for row in existing_data:
        print(row)
    
    # Move the cursor to the end of the file to append new data
    csv_file.seek(0, 2)  # Move to the end of the file
    writer = csv.writer(csv_file)
    new_data = [["John", 35, "Hyderabad"]]
    writer.writerows(new_data)

# creating csv file w+
import csv
# Writing and reading a CSV file using w+ mode
with open('data_w_plus.csv', 'w+', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Write initial data
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 29, "Pune"])
    
    # Move the cursor back to the beginning of the file to read
    csv_file.seek(0)
    reader = csv.reader(csv_file)
    print("Data in data_w_plus.csv:")
    for row in reader:
        print(row)


#json file operations
import json
# Writing to a JSON file
data = {
    "name": "Deepika",
    "age": 24,
    "city": "Delhi"
}
with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
# Reading from a JSON file
with open('data.json', 'r') as json_file:
    data_loaded = json.load(json_file)
    print(data_loaded)

#reading json file
with open('data.json', 'r') as json_file:
    data_loaded = json.load(json_file)
    print("Name:", data_loaded['name'])
    print("Age:", data_loaded['age'])
    print("City:", data_loaded['city'])

# Appending to a JSON file
import json
data_to_append = {
    "name": "Rahul",
    "age": 30,
    "city": "Mumbai"
}
with open('data.json', 'r+') as json_file:
    # Load existing data
    data_loaded = json.load(json_file)
    
    # Append new data
    data_loaded.update(data_to_append)
    
    # Move the cursor back to the beginning of the file to overwrite
    json_file.seek(0)
    json.dump(data_loaded, json_file, indent=4)
    json_file.truncate()  # Remove any leftover data from previous content

# Reading and writing to a JSON file using r+ mode
with open('data.json', 'r+') as json_file:
    # Load existing data
    data_loaded = json.load(json_file)
    print("Existing data:", data_loaded)
    
    # Append new data
    new_data = {
        "name": "Anjali",
        "age": 22,
        "city": "Bangalore"
    }
    data_loaded.update(new_data)
    
    # Move the cursor back to the beginning of the file to overwrite
    json_file.seek(0)
    json.dump(data_loaded, json_file, indent=4)
    json_file.truncate()  # Remove any leftover data from previous content

# Writing and reading a JSON file using w+ mode
with open('data_w_plus.json', 'w+') as json_file:
    # Write initial data
    initial_data = {
        "name": "Alice",
        "age": 29,
        "city": "Pune"
    }
    json.dump(initial_data, json_file, indent=4)
    
    # Move the cursor back to the beginning of the file to read
    json_file.seek(0)
    data_loaded = json.load(json_file)
    print("Data in data_w_plus.json:", data_loaded)

# Appending to a JSON file using a+ mode
import json
import os

filename = 'data_w_plus.json'

# Step 1: Create file with empty list if it doesn't exist
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        json.dump([], f)

# Step 2: Load existing list data
with open(filename, 'r') as file:
    try:
        data = json.load(file)
        if not isinstance(data, list):
            data = [data]  # Convert dict to list of dicts
    except json.JSONDecodeError:
        data = []

# Step 3: Append new dictionary to list
new_data = {"name": "Alice", "age": 29, "city": "Pune"}
data.append(new_data)

# Step 4: Save the updated list
with open(filename, 'w') as file:
    json.dump(data, file, indent=4)


