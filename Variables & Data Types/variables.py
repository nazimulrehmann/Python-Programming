''' 
Variables in Python Programming:
    Variables are fundamental building blocks in Python (and all programming languages) 
    that allow you to store and manipulate data. They act as named containers that hold 
    values which can be accessed and modified throughout your program.

A variable is:
    A named reference to a value stored in memory
    Like a labeled box where you can store information
    Can hold different types of data (numbers, text, lists, etc.)
    Can be changed (varied) during program execution
    
Python has some rules for naming variables:
   Must start with a letter (a-z, A-Z) or underscore (_)
   Can contain letters, numbers, and underscores
   Cannot be a Python keyword (like if, for, while, etc.)
   Case-sensitive (age, Age, and AGE are different variables)
'''

# In Python, we can create a variable by assigning a value to it using assignment `=` operator:

# Syntax: variable_name = value ( i: e  string, integers, float,& boolean )

# Examples:
name = "Nazim"          # String variable
age = 25               # Integer variable
height = 5.9           # Float variable
is_student = True      # Boolean variable


# Variable Types
# Python variables can hold different data types:

# a) Numbers:
count = 10          # Integer
price = 19.99       # Float
complex_num = 3 + 4j  # Complex number

# b) strings:
greeting = "Hello, World!"
single_char = 'a'
multi_line = """This is a
                multi-line string"""
                
# c) booleans:
is_active = True
has_permission = False                

# d) sequences:
fruits = ["apple", "banana", "cherry"]  # List
coordinates = (10, 20)                  # Tuple
unique_numbers = {1, 2, 3}              # Set

# e) mappings:
person = {"name": "Bob", "age": 30}     # Dictionary



# Variable Reassignment
# You can change the value of a variable by assigning a new value to it:
# Python is dynamically typed, meaning you don't need to declare variable types

score = 10
print(score)  # Output: 10

score = 20    # Reassigning
print(score)  # Output: 20

# You can even change the data type
score = "High Score"
print(score)  # Output: High Score


# The same variable can hold different types
item = 42        # Now it's an integer
item = "Answer"  # Now it's a string
item = 42.0      # Now it's a float


# Multiple Assignment
# Python allows you to assign multiple variables at once:

# Assigning multiple variables to different values
x, y, z = 10, 20, 30
print(x, y, z)  # Output: 10 20 30

# Assigning the same value to multiple variables
a = b = c = 100
print(a, b, c)  # Output: 100 100 100


# Variable Swapping
# Python makes it easy to swap variable values:

first = "apple"
second = "orange"

# Swap values
first, second = second, first

print(first)   # Output: orange
print(second)  # Output: apple


# Constants
# While Python doesn't have true constants, variables with all uppercase names are conventionally
# treated as constants (though they can still be changed):
PI = 3.14159
MAX_USERS = 100


# Variable Scope
# Variables have different scopes (where they can be accessed):

# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    
my_function()
# print(local_var)  # Error - can't access local outside function

