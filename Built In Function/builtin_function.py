# Python Built-in Functions and Advanced Concepts

# Basic Built-in Functions

# 1. abs()
# Returns the absolute value of a number.
print(abs(-5))  # Output: 5
print(abs(3.14))  # Output: 3.14

# 2. all()
# Returns True if all elements in the iterable are true (or if the iterable is empty).
print(all([True, 1, "hello"]))  # Output: True
print(all([True, 0, "hello"]))  # Output: False

# 3. any()
# Returns True if any element in the iterable is true.
print(any([False, 0, ""]))  # Output: False
print(any([False, 1, ""]))  # Output: True

# 4. ascii()
# Returns a string containing a printable representation of an object.
print(ascii("pythön"))  # Output: 'pyth\xf6n'

# 5. bin()
# Converts an integer to a binary string.
print(bin(10))  # Output: '0b1010'

# 6. bool()
# Converts a value to a Boolean.
print(bool(1))  # Output: True
print(bool(0))  # Output: False
print(bool(""))  # Output: False

# 7. breakpoint()
# Drops into the debugger at the call site (Python 3.7+).
# breakpoint()  # Uncomment to enter debugger

# 8. bytearray()
# Returns a mutable bytearray object.
print(bytearray([1, 2, 3]))  # Output: bytearray(b'\x01\x02\x03')

# 9. bytes()
# Returns an immutable bytes object.
print(bytes([1, 2, 3]))  # Output: b'\x01\x02\x03'

# 10. callable()
# Returns True if the object appears callable.
print(callable(print))  # Output: True
print(callable(5))      # Output: False

# 11. chr()
# Returns the string representing a character whose Unicode code is the integer.
print(chr(65))  # Output: 'A'

# 12. classmethod()
# Transforms a method into a class method.
class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")

MyClass.class_method()

# 13. compile()
# Compiles source into a code or AST object.
code = compile('print("Hello")', 'test', 'exec')
exec(code)  # Output: Hello

# 14. complex()
# Creates a complex number.
print(complex(2, 3))  # Output: (2+3j)

# 15. delattr()
# Deletes the named attribute from the object.
class MyClass:
    x = 10

obj = MyClass()
delattr(obj, 'x')

# 16. dict()
# Creates a dictionary.
print(dict(a=1, b=2))  # Output: {'a': 1, 'b': 2}

# 17. dir()
# Returns the list of names in the current local scope or attributes of an object.
print(dir([]))  # Output: list of list methods

# 18. divmod()
# Returns a pair of numbers (quotient, remainder).
print(divmod(10, 3))  # Output: (3, 1)

# 19. enumerate()
# Returns an enumerate object.
for i, v in enumerate(['a', 'b', 'c']):
    print(i, v)
# Output:
# 0 a
# 1 b
# 2 c

# 20. eval()
# Evaluates a string as Python code.
print(eval('2 + 2'))  # Output: 4

# 21. exec()
# Executes dynamically created Python code.
exec('print("Hello World")')  # Output: Hello World

# 22. filter()
# Constructs an iterator from elements of iterable for which function returns true.
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2])))  # Output: [1, 2]

# 23. float()
# Converts a number or string to a float.
print(float('3.14'))  # Output: 3.14

# 24. format()
# Formats a value into a specified format.
print(format(123, '05d'))  # Output: '00123'
print(format(3.14159, '.2f'))  # Output: '3.14'

# 25. frozenset()
# Returns a new frozenset object.
print(frozenset([1, 2, 3]))  # Output: frozenset({1, 2, 3})

# 26. getattr()
# Returns the value of the named attribute of object.
class MyClass:
    x = 10

print(getattr(MyClass, 'x'))  # Output: 10

# 27. globals()
# Returns the dictionary representing the current global symbol table.
print(globals())

# 28. hasattr()
# Returns True if the object has the named attribute.
class MyClass:
    x = 10

print(hasattr(MyClass, 'x'))  # Output: True

# 29. hash()
# Returns the hash value of the object.
print(hash('hello'))  # Output: hash value (varies)

# 30. help()
# Invokes the built-in help system.
# help(list)  # Uncomment to see list help

# 31. hex()
# Converts an integer to a lowercase hexadecimal string.
print(hex(255))  # Output: '0xff'

# 32. id()
# Returns the identity of an object.
x = 5
print(id(x))  # Output: memory address

# 33. input()
# Reads a string from standard input.
# name = input("Enter your name: ")

# 34. int()
# Converts a number or string to an integer.
print(int('10'))  # Output: 10
print(int(3.14))  # Output: 3

# 35. isinstance()
# Returns True if the object is an instance of the class.
print(isinstance(5, int))  # Output: True

# 36. issubclass()
# Returns True if the class is a subclass of another class.
print(issubclass(bool, int))  # Output: True

# 37. iter()
# Returns an iterator object.
my_iter = iter([1, 2, 3])
print(next(my_iter))  # Output: 1

# 38. len()
# Returns the length of an object.
print(len([1, 2, 3]))  # Output: 3

# 39. list()
# Creates a list.
print(list((1, 2, 3)))  # Output: [1, 2, 3]

# 40. locals()
# Updates and returns a dictionary representing the current local symbol table.
def my_func():
    x = 10
    print(locals())

my_func()  # Output: {'x': 10}

# 41. map()
# Applies function to every item of iterable and returns a list of the results.
print(list(map(lambda x: x*2, [1, 2, 3])))  # Output: [2, 4, 6]

# 42. max()
# Returns the largest item in an iterable.
print(max([1, 2, 3]))  # Output: 3

# 43. memoryview()
# Returns a memory view object.
v = memoryview(b'abcd')
print(v[0])  # Output: 97

# 44. min()
# Returns the smallest item in an iterable.
print(min([1, 2, 3]))  # Output: 1

# 45. next()
# Retrieves the next item from an iterator.
my_iter = iter([1, 2, 3])
print(next(my_iter))  # Output: 1

# 46. object()
# Returns a new featureless object.
obj = object()

# 47. oct()
# Converts an integer to an octal string.
print(oct(8))  # Output: '0o10'

# 48. open()
# Opens a file and returns a file object.
# f = open('file.txt', 'r')

# 49. ord()
# Returns the Unicode code point for a one-character string.
print(ord('A'))  # Output: 65

# 50. pow()
# Returns x to the power y.
print(pow(2, 3))  # Output: 8

# 51. print()
# Prints objects to the text stream file.
print("Hello", "World", sep=', ')  # Output: Hello, World

# 52. property()
# Returns a property attribute.
class MyClass:
    def __init__(self):
        self._x = None
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value

obj = MyClass()
obj.x = 10
print(obj.x)  # Output: 10

# 53. range()
# Returns a sequence of numbers.
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

# 54. repr()
# Returns a string containing a printable representation of an object.
print(repr('hello'))  # Output: "'hello'"

# 55. reversed()
# Returns a reverse iterator.
print(list(reversed([1, 2, 3])))  # Output: [3, 2, 1]

# 56. round()
# Rounds a number to a given precision.
print(round(3.14159, 2))  # Output: 3.14

# 57. set()
# Creates a set.
print(set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# 58. setattr()
# Sets the named attribute on the given object to the specified value.
class MyClass:
    pass

obj = MyClass()
setattr(obj, 'x', 10)
print(obj.x)  # Output: 10

# 59. slice()
# Returns a slice object.
my_list = [0, 1, 2, 3, 4]
print(my_list[slice(1, 4)])  # Output: [1, 2, 3]

# 60. sorted()
# Returns a new sorted list from the items in iterable.
print(sorted([3, 1, 2]))  # Output: [1, 2, 3]

# 61. staticmethod()
# Transforms a method into a static method.
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.static_method()

# 62. str()
# Returns a string version of an object.
print(str(123))  # Output: '123'

# 63. sum()
# Sums the items of an iterable.
print(sum([1, 2, 3]))  # Output: 6

# 64. super()
# Returns a proxy object that delegates method calls to a parent or sibling class.
class Parent:
    def method(self):
        print("Parent method")

class Child(Parent):
    def method(self):
        super().method()
        print("Child method")

Child().method()

# 65. tuple()
# Creates a tuple.
print(tuple([1, 2, 3]))  # Output: (1, 2, 3)

# 66. type()
# Returns the type of an object or creates a new type.
print(type(5))  # Output: <class 'int'>

# 67. vars()
# Returns the __dict__ attribute for a module, class, instance, or any other object.
class MyClass:
    def __init__(self):
        self.x = 10

print(vars(MyClass()))  # Output: {'x': 10}

# 68. zip()
# Makes an iterator that aggregates elements from each of the iterables.
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# 69. __import__()
# Advanced function called by the import statement (rarely used directly).
math = __import__('math')
print(math.sqrt(4))  # Output: 2.0

# Advanced Built-in Functions and Concepts

# 1. Decorators
# Functions that modify the behavior of other functions.
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# 2. Generators
# Functions that return an iterator using yield.
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(list(counter))  # Output: [1, 2, 3, 4, 5]

# 3. Context Managers (with statement)
# Manages resources properly.
# Using with statement for file handling
with open('file.txt', 'r') as f:
    content = f.read()

# Creating custom context manager
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

with MyContextManager() as cm:
    print("Inside context")

# 4. Lambda Functions
# Anonymous functions.
square = lambda x: x**2
print(square(5))  # Output: 25

# 5. Closures
# Functions that remember values in enclosing scopes.
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure = outer_func(10)
print(closure(5))  # Output: 15

# 6. functools Module
# Higher-order functions and operations on callable objects.
from functools import partial, reduce, wraps

# Partial function application
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # Output: 25

# Reduce function
print(reduce(lambda x, y: x+y, [1, 2, 3, 4]))  # Output: 10

# Wraps for preserving metadata
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

# 7. itertools Module
# Functions creating iterators for efficient looping.
import itertools

# Infinite iterators
counter = itertools.count(start=10, step=2)
print(next(counter), next(counter))  # Output: 10 12

# Combinatoric iterators
print(list(itertools.permutations([1, 2, 3], 2)))
# Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# 8. collections Module
# Specialized container datatypes.
from collections import namedtuple, defaultdict, Counter, deque

# Named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20

# Default dict
dd = defaultdict(int)
dd['key'] += 1
print(dd['key'])  # Output: 1

# Counter
cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(cnt)  # Output: Counter({'blue': 3, 'red': 2, 'green': 1})

# Deque
d = deque([1, 2, 3])
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3])

# 9. operator Module
# Function equivalents to built-in operators.
from operator import add, mul, itemgetter, attrgetter

print(add(1, 2))  # Output: 3
print(mul(2, 3))  # Output: 6

# For sorting
people = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 20}]
print(sorted(people, key=itemgetter('age')))
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person('Alice', 25), Person('Bob', 20)]
print(sorted(people, key=attrgetter('age')))

# 10. contextlib Module
# Utilities for with-statement contexts.
from contextlib import contextmanager

@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('Hello, world!')

# 11. asyncio Module
# Asynchronous I/O, event loop, coroutines and tasks.
import asyncio

async def hello_world():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(hello_world())

# 12. typing Module
# Support for type hints.
from typing import List, Dict, Tuple, Optional, Union, Callable

def greeting(name: str) -> str:
    return 'Hello ' + name

Vector = List[float]
ConnectionOptions = Dict[str, str]
Response = Union[str, bytes]

# 13. dataclasses Module
# Decorator to automatically add special methods to classes.
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # Default value

p = Point(1.5, 2.5)
print(p)  # Output: Point(x=1.5, y=2.5, z=0.0)

# 14. enum Module
# Support for enumerations.
from enum import Enum, auto

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)  # Output: Color.RED
print(Color.RED.value)  # Output: 1

class AutoColor(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

# 15. abc Module
# Abstract base classes.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

# shape = Shape()  # Raises TypeError
square = Square(5)
print(square.area())  # Output: 25

# 16. pathlib Module
# Object-oriented filesystem paths.
from pathlib import Path

p = Path('/home/user/documents')
print(p / 'file.txt')  # Output: /home/user/documents/file.txt
print(p.exists())  # Output: True or False

# 17. concurrent.futures Module
# High-level interface for asynchronously executing callables.
from concurrent.futures import ThreadPoolExecutor, as_completed

def square(x):
    return x * x

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(square, i) for i in range(5)]
    for future in as_completed(futures):
        print(future.result())

# 18. json Module
# JSON encoder and decoder.
import json

data = {'name': 'John', 'age': 30, 'city': 'New York'}
json_str = json.dumps(data)
print(json_str)  # Output: {"name": "John", "age": 30, "city": "New York"}

data_back = json.loads(json_str)
print(data_back)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# 19. pickle Module
# Python object serialization.
import pickle

data = {'a': [1, 2, 3], 'b': ('string', 'another string')}
pickled_data = pickle.dumps(data)
unpickled_data = pickle.loads(pickled_data)
print(unpickled_data)  # Output: {'a': [1, 2, 3], 'b': ('string', 'another string')}

# 20. logging Module
# Flexible event logging system.
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('This is an info message')
logger.warning('This is a warning message')

# Important Fundamentals

# 1. Mutable vs Immutable Objects
# Mutable: list, dict, set, bytearray
# Immutable: int, float, str, tuple, frozenset, bytes

# 2. Pass by Object Reference
# Python passes arguments by object reference (value for immutable objects, reference for mutable)

# 3. Duck Typing
# "If it looks like a duck and quacks like a duck, it's a duck"
# Focus on behavior rather than type

# 4. EAFP vs LBYL
# Easier to Ask for Forgiveness than Permission (try/except)
# Look Before You Leap (checking before operations)

# 5. Garbage Collection
# Reference counting + generational garbage collection
# `gc` module for manual control

# 6. Global Interpreter Lock (GIL)
# Only one thread executes Python bytecode at a time
# Impacts CPU-bound multithreading performance

# 7. Metaclasses
# Classes are instances of type (or another metaclass)
# Can customize class creation

# 8. Descriptors
# Protocol that allows customized attribute access
# Used to implement properties, methods, static methods, class methods

# 9. Method Resolution Order (MRO)
# Determines the order in which base classes are searched for attributes
# Uses C3 linearization algorithm

# 10. Python's Data Model
# Special methods (__init__, __str__, __add__, etc.)
# Protocol-based (implement methods to support operations)