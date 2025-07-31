# Conditional Statements in Python: `if`, `else`, and `elif`
# Conditional statements allow your program to make decisions based on certain conditions.
# Python provides several conditional statements:

'''
Basic Structure

if condition:
    # code to execute if condition is True

if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False

if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
else:
    # code to execute if all above conditions are False
'''

# Exercises with User Input

# Exercise 1: Simple if-else (Comparison operators)
# Check if a number is positive or negative

num = float(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Exercise 2: Multiple conditions (Logical operators)
# Check if a number is between 1 and 100

num = int(input("Enter a number between 1 and 100: "))

if num >= 1 and num <= 100:
    print("Valid number")
else:
    print("Number out of range")

# Exercise 3: elif ladder
# Grade calculator

score = float(input("Enter your score (0-100): "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is {grade}")

# Exercise 4: Combining operators
# Check if a year is a leap year

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Exercise 5: String comparison
# Simple password checker

password = input("Enter password: ")

if len(password) < 6:
    print("Password too short (min 6 characters)")
elif password == "password":
    print("Too obvious! Choose a better password")
else:
    print("Password accepted")


# Exercise 6: Nested if statements
# Ticket price calculator

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower()

if age < 5:
    price = 0
else:
    if age <= 18 or is_student == 'yes':
        price = 10
    elif age > 60:
        price = 12
    else:
        price = 20

print(f"Your ticket price is ${price}")


#Exercise 7: Complex conditions
# Number properties checker

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print(f"{num} is even")
    if num % 4 == 0:
        print(f"{num} is divisible by 4")
else:
    print(f"{num} is odd")
    if num % 3 == 0:
        print(f"{num} is divisible by 3")