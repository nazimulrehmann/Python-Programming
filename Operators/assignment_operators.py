# Assignment Operators in Python
# Assignment operators are used to assign values to variables. 
# Python provides several assignment operators that combine arithmetic or bitwise operations with assignment for more concise code.

# Basic Assignment Operator (=)

# The simple assignment operator assigns a value to a variable.
x = 10  # Assigns the value 10 to variable x
print(x)  # Output: 10


# Compound Assignment Operators
# These operators combine an arithmetic/bitwise operation with assignment.

# Addition Assignment (+=)
# Adds the right operand to the left operand and assigns the result to the left operand.

x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8


# Subtraction Assignment (-=)
# Subtracts the right operand from the left operand and assigns the result.

x = 10
x -= 4  # Equivalent to x = x - 4
print(x)  # Output: 6

# Multiplication Assignment (*=)
# Multiplies the left operand with the right operand and assigns the result.

x = 7
x *= 2  # Equivalent to x = x * 2
print(x)  # Output: 14

# Division Assignment (/=)
# Divides the left operand by the right operand and assigns the result (always float).

x = 15
x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 5.0

# Floor Division Assignment (//=)
# Performs floor division and assigns the integer result.

x = 17
x //= 5  # Equivalent to x = x // 5
print(x)  # Output: 3

# Modulus Assignment (%=)
# Performs modulus operation and assigns the remainder.

x = 17
x %= 5  # Equivalent to x = x % 5
print(x)  # Output: 2

# Exponentiation Assignment (**=)
# Raises the left operand to the power of the right operand and assigns the result.

x = 2
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 8


# Bitwise AND Assignment (&=)
# Performs bitwise AND and assigns the result.
x = 10  # 1010
x &= 4  # 0100, Equivalent to x = x & 4
print(x)  # Output: 0 (0000)


# Bitwise OR Assignment (|=)
# Performs bitwise OR and assigns the result.
x = 10  # 1010
x |= 4  # 0100, Equivalent to x = x | 4
print(x)  # Output: 14 (1110)


# Bitwise XOR Assignment (^=)
# Performs bitwise XOR and assigns the result.

x = 10  # 1010
x ^= 6  # 0110, Equivalent to x = x ^ 6
print(x)  # Output: 12 (1100)

# Right Shift Assignment (>>=)
# Performs bitwise right shift and assigns the result.

x = 8  # 1000
x >>= 2  # Equivalent to x = x >> 2
print(x)  # Output: 2 (0010)

# Left Shift Assignment (<<=)
# Performs bitwise left shift and assigns the result.

x = 2  # 0010
x <<= 3  # Equivalent to x = x << 3
print(x)  # Output: 16 (10000)


# Multiple Assignments
# Python allows multiple assignments in a single line:

a, b, c = 5, 10, 15  # Assigns 5 to a, 10 to b, 15 to c
print(a, b, c)  # Output: 5 10 15

# Swapping variables
x, y = 10, 20
x, y = y, x  # Swaps values
print(x, y)  # Output: 20 10

# Chained Assignments
# Assign the same value to multiple variables:

x = y = z = 0  # All three variables get value 0
print(x, y, z)  # Output: 0 0 0


# Exercises with Solutions

# Exercise 1: Basic Operations
a = 10
a += 5
a -= 3
a *= 2
a /= 4
print(a)  # What's the output?

# Solution:
# a = 10
# a += 5 → a = 15
# a -= 3 → a = 12
# a *= 2 → a = 24
# a /= 4 → a = 6.0
# Output: 6.0

# Exercise 2: Bitwise Operations
x = 12  # 1100
x &= 5  # 0101
x |= 9  # 1001
print(x)  # What's the output?


# Solution:
# x = 12 (1100)
# x &= 5 → 1100 & 0101 = 0100 (4)
# x |= 9 → 0100 | 1001 = 1101 (13)
# Output: 13


# Exercise 3: Shift Operations

y = 4
y <<= 2
y >>= 1
print(y)  # What's the output?


# Solution:

# y = 4 (0100)
# y <<= 2 → 0100 << 2 = 010000 (16)
#  y >>= 1 → 010000 >> 1 = 01000 (8)
# Output: 8


# Practical Examples

# Example 1: Accumulating Values
total = 0
for i in range(1, 6):
    total += i
print(total)  # Output: 15 (1+2+3+4+5)


#Example 2: Doubling Until Threshold
value = 1
while value < 100:
    print(value)
    value *= 2
# Output: 1, 2, 4, 8, 16, 32, 64

# Example 3: Converting Seconds to Minutes and Seconds
seconds = 135
minutes = 0
minutes += seconds // 60
seconds %= 60
print(f"{minutes} minutes and {seconds} seconds")
# Output: "2 minutes and 15 seconds"

# Important Notes

#  Assignment operators have very low precedence (only higher than comma)
#  The right-hand side is evaluated first
#  Augmented assignments (+=, -= etc.) are more efficient than their expanded forms
#  Assignment operators can be used with mutable objects (like lists) to modify them in-place