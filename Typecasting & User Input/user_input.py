# User Inputs in Python
# Python uses the input() function to get user input from the console.

# Basic Input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Important Characteristics of input():

# a) Always returns a string (even for numbers)
# b) Can display a prompt message
# c) Execution pauses until user presses Enter
# d) To get numeric input, you must cast the result

# Getting Different Input Types:

# String input (default)
text = input("Enter some text: ")

# Integer input
age = int(input("Enter your age: "))

# Float input
price = float(input("Enter price: "))

# Multiple values in one input
values = input("Enter two numbers separated by space: ")
num1, num2 = map(float, values.split())

# Handling Input Errors
# Always validate user input to prevent crashes:

while True:
    try:
        age = int(input("Enter your age: "))
        break  # Exit loop if conversion succeeds
    except ValueError:
        print("Please enter a valid integer!")
        
        
        
# Advanced Input Techniques

# a) multiple inputs at once:
# Split into list
numbers = input("Enter numbers separated by commas: ").split(',')
numbers = [int(num) for num in numbers]

# b) password input (hidden): 
import getpass
password = getpass.getpass("Enter password: ")

# c) menu selection:
print("1. Option 1")
print("2. Option 2")
choice = input("Select an option (1-2): ")


# Practical Example:

# a) Simple Calculator:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum: {num1 + num2}") 

# b) User Registration:
username = input("Create username: ")
password = input("Create password: ")
age = int(input("Enter age: "))
print(f"User {username} created! Age: {age}")

# c) Temperature Converter:
fahrenheit = float(input("Enter temperature in °F: "))
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.2f}°C")

# Combining Type Casting and Input

# this is where these concepts work together most importantly: 
# Without casting - string concatenation
num1 = input("Enter a number: ")  # "5"
num2 = input("Enter another: ")   # "3"
print(num1 + num2)  # "53" (string concatenation)

# With casting - numeric addition
num1 = int(input("Enter a number: "))  # 5
num2 = int(input("Enter another: "))   # 3
print(num1 + num2)  # 8 (numeric addition)