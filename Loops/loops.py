# Python Loops: From Basics to Advanced Concepts
# Loops are fundamental constructs in Python (and all programming languages)
# that allow you to execute a block of code repeatedly. Let's explore Python loops in increasing levels of sophistication.

# Basic Loop Structures

# `for` Loop
# The `for` loop iterates over items of any sequence (list, tuple, string, etc.) in the order they appear.

# Basic for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


# `while` Loop
# The `while` loop executes as long as a condition is true.


# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

#  Loop Control Statements

# `break`
# Terminates the loop immediately.


for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0-4


# `continue`
# Skips the rest of the current iteration and moves to the next.

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # Prints odd numbers 1,3,5,7,9

### `else` Clause
# Executed when the loop completes normally (not via `break`).


for i in range(5):
    print(i)
else:
    print("Loop completed successfully")


# Intermediate Loop Concepts
"""
# Nested Loops

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# The `range()` Function
# Creates a sequence of numbers.

for i in range(5):          # 0 to 4
for i in range(2, 6):       # 2 to 5
for i in range(0, 10, 2):   # 0,2,4,6,8

# Enumerating with `enumerate()`
# Get both index and value:


for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)
"""

# Looping through multiple sequences with `zip()`


names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")


# Advanced Loop Techniques

# List Comprehensions
# Concise way to create lists.


squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]


# Dictionary Comprehensions


square_dict = {x: x**2 for x in range(5)}


# Generator Expressions
# Memory-efficient alternative to list comprehensions.


sum_of_squares = sum(x**2 for x in range(1000000))  # Doesn't create a list


# The `itertools` Module
# Powerful loop tools from the standard library.

import itertools

# Infinite counting
for i in itertools.count(10):
    if i > 15:
        break
    print(i)

# All possible combinations
for combo in itertools.combinations('ABCD', 2):
    print(combo)

# Performance Considerations

### Loop Optimization
# - Move calculations outside loops when possible
# - Use built-in functions over manual loops
# - Consider list comprehensions for simple transformations

# Less efficient
result = []
for x in some_list:
    result.append(complex_calculation(x))

# More efficient
result = [complex_calculation(x) for x in some_list]