# Arithmetic Operators in Python

# Arithmetic operators are used to perform mathematical operations on numerical values
# (both integers and floating-point numbers). Python provides several arithmetic operators
# that are fundamental to performing calculations in your programs.

# Basic Arithmetic Operators

# Addition (+)
# Adds two operands together.

x = 5
y = 3
result = x + y  # 5 + 3 = 8
print(result)   # Output: 8

# Subtraction (-)
# Subtracts the right operand from the left operand.

x = 10
y = 4
result = x - y  # 10 - 4 = 6
print(result)   # Output: 6

# Multiplication (*)
# Multiplies two operands.

x = 7
y = 6
result = x * y  # 7 * 6 = 42
print(result)   # Output: 42

# Division (/)
# Divides the left operand by the right operand. Always returns a float.

x = 15
y = 4
result = x / y  # 15 / 4 = 3.75
print(result)   # Output: 3.75


# Floor Division (//)
# Divides and returns the integer value of the quotient (drops any fractional part).

x = 17
y = 5
result = x // y  # 17 // 5 = 3 (not 3.4)
print(result)    # Output: 3


# Modulus (%)
# Returns the remainder of division.

x = 17
y = 5
result = x % y  # 17 % 5 = 2 (since 5*3=15 and 17-15=2)
print(result)   # Output: 2


# Exponentiation (**)
# Raises the left operand to the power of the right operand.

x = 2
y = 5
result = x ** y  # 2^5 = 32
print(result)    # Output: 32


# Special Cases and Behaviors

# Operator Precedence
# Python follows standard mathematical operator precedence:
# Parentheses `()` (highest precedence)
# Exponentiation `**`
# Multiplication `*`, Division `/`, Floor Division `//`, Modulus `%`
# Addition `+`, Subtraction `-` (lowest precedence)

result = 10 + 3 * 2 ** 2  # 3*4=12, then 10+12=22
print(result)  # Output: 22

result = (10 + 3) * 2 ** 2  # 10+3=13, 2^2=4, then 13*4=52
print(result)  # Output: 52


# Division by Zero
# Attempting to divide by zero raises a `ZeroDivisionError`:

# This will cause an error
# result = 5 / 0

# Mixed Operand Types
# When operating on mixed types (int and float), Python converts the result to float:

result = 5 + 3.5  # int + float = float
print(result)     # Output: 8.5


# Negative Numbers
# All operators work with negative numbers as expected:

print(-5 * 3)    # Output: -15
print(10 / -2)   # Output: -5.0
print(-2 ** 3)   # Output: -8 (exponentiation has higher precedence than negation)


# Practical Examples

# Calculating Area
length = 10
width = 5
area = length * width
print(f"Area of rectangle: {area}")  # Output: Area of rectangle: 50


# Converting Temperature
fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F is {celsius:.2f}°C")  # Output: 98.6°F is 37.00°C

# Checking Even/Odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")  # Output: Odd


# Compound Interest
principal = 1000
rate = 0.05
years = 3
amount = principal * (1 + rate) ** years
print(f"Future amount: ${amount:.2f}")  # Output: Future amount: $1157.63


#  Understanding these arithmetic operators is fundamental to performing calculations and building more complex algorithms in Python.