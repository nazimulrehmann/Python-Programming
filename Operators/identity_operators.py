# Identity Operators in Python
# Identity operators are used to compare the memory locations of two objects to determine 
# if they are the same object. Unlike comparison operators which check for equality of values,
# identity operators check whether two variables refer to the same object in memory.

# Python has two identity operators:

#  `is` - Returns `True` if both variables point to the same object
#  `is not` - Returns `True` if both variables do not point to the same object

# Key Characteristics:
# - Identity operators compare memory addresses, not values
# - They are useful when you need to check if two variables reference exactly the same object
# - For value comparison, you should use `==` instead of `is`

# How Identity Operators Work
a = [1, 2, 3]
b = a       # b references the same object as a
c = [1, 2, 3]  # c is a different object with same content

print(a is b)     # True - same object
print(a is c)     # False - different objects
print(a == c)     # True - same content


# When to Use Identity Operators
'''
 Checking for `None`
      if x is None: 
      if x is not None:
'''

#  Working with singletons (like `True`, `False`, `None`)
#  When you specifically need to check object identity rather than equality

# Important Note about Small Integers and Strings

# Python caches small integers (-5 to 256) and some strings for optimization, which can lead to unexpected behavior:

a = 256
b = 256
print(a is b)  # True - cached integer

a = 257
b = 257
print(a is b)  # False - not cached (may vary by implementation)


# Exercises

# Exercise 1: Basic Identity Check

x = ["apple", "banana"]
y = x
z = ["apple", "banana"]

print(x is y)  # What will this output?
print(x is z)  # What will this output?
print(x == z)  # What will this output?


# Exercise 2: None Check

def process_data(data):
    if data is None:
        print("No data provided")
    else:
        print(f"Processing {data}")

process_data(None)
process_data("Sample data")

# Exercise 3: Integer Identity

a = 1000
b = 1000
print(a is b)  # What will this output? Why?

a = 10
b = 10
print(a is b)  # What will this output? Why?


# Exercise 4: String Identity

s1 = "hello"
s2 = "hello"
s3 = "hello world"[:5]  # "hello"

print(s1 is s2)  # What will this output?
print(s1 is s3)  # What will this output?


# Exercise 5: Custom Objects

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = Person("Alice")
p3 = p1

print(p1 is p2)  # What will this output?
print(p1 is p3)  # What will this output?

# Exercise 6: Identity vs Equality
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)  # What will this output?
print(list1 is list2)  # What will this output?
print(list1 is list3)  # What will this output?