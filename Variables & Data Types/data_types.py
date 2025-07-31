# Data Types in Python:  
  # In Python, data types define the kind of value a variable can hold. Python is dynamically typed,
  # meaning the interpreter automatically assigns a data type based on the value.

# Numeric Data Types
# a) int (Integer)
# Represents whole numbers (positive or negative).
# No decimal points.
# Example:

age = 25  
temperature = -10  
print(type(age))  # Output: <class 'int'>

# b) float (Floating Point)
# Represents decimal numbers.
# Example:

price = 19.99  
pi = 3.14159  
print(type(price))  # Output: <class 'float'>

# c) complex (Complex Numbers)
# Used in advanced mathematics.
# Written as a + bj where a = real part, b = imaginary part.
# Example:

complex_num = 3 + 5j
print(type(complex_num))  # <class 'complex'>

# Boolean Data Type (bool):
# Represents True or False (used in conditions).
# Example:

is_raining = True  
is_logged_in = False  
print(type(is_raining))  # Output: <class 'bool'>


# Sequence Data Types (Ordered Collections)
# a) str (String)
# Represents text (enclosed in " " or ' ').
# Immutable (cannot change after creation).
# Example:

name = "Alice"  
greeting = 'Hello, World!'  
print(type(name))  # Output: <class 'str'>


# b) list (Lists are mutable)
# Ordered, changeable collection.
# Allows duplicate elements.
# Example:

fruits = ["apple", "banana", "cherry"]  
fruits[0] = "orange"  # Modifying is allowed  
print(type(fruits))  # Output: <class 'list'>

# c) Tuple (immutable)
# Ordered, unchangeable collection.
# Faster than lists (immutable).
# Example:

coordinates = (10.0, 20.0)  
# coordinates[0] = 5.0  ❌ Error (cannot modify)  
print(type(coordinates))  # Output: <class 'tuple'>

# Mapping Type (dict - Dictionary)
# Stores key-value pairs (like a real dictionary).
# Unordered but changeable.
# Example:

person = {"name": "John", "age": 30}  
print(person["name"])  # Output: "John"  
print(type(person))  # Output: <class 'dict'>

# Set Types (Unordered, Unique Elements)
# a) set (Set)
# Unordered, mutable, and contains unique elements.
# Example:
 
unique_numbers = {1, 2, 3, 2, 1}  # Becomes {1, 2, 3}  
unique_numbers.add(4)  # Can modify  
print(type(unique_numbers))  # Output: <class 'set'>
 
#b) frozenset (Frozen Set)
# Immutable version of a set.
# Example:

frozen = frozenset({"a", "b", "c"})  
# frozen.add("d") ❌ Error (cannot modify)  
print(type(frozen))  # Output: <class 'frozenset'>


# Binary Types (For Raw Byte Data)
# a) bytes
# Immutable sequence of bytes (0-255).
# Used in file handling, networking.
# Example:

data = b"Hello"  
print(type(data))  # Output: <class 'bytes'>

# b) bytearray
# Mutable version of bytes.
# Example:

mutable_data = bytearray(b"Hello")  
mutable_data[0] = 72  # Can modify  
print(type(mutable_data))  # Output: <class 'bytearray'>

# c) memoryview
# Used for memory-efficient access to binary data.
# Example:

mem_view = memoryview(bytes(5))  
print(type(mem_view))  # Output: <class 'memoryview'>

# None Type (None)
# Represents absence of value or empty.
# Example:

result = None  
print(type(result))  # Output: <class 'NoneType'>