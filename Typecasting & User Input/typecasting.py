'''
Type Casting (Type Conversion):
   Type casting is the process of converting a variable from one data type to another. 
   Python provides built-in functions for converting between different types.
   
Implicit & Explicit Type Casting:
   Implicit Type Casting: Done automatically by Python
   Explicit Type Casting: Done manually by the programmer
'''
# Common Type Casting Functions

# Function	   Description      	        Example

# int()       Converts to integer	      int("10") → 10
# float()	  Converts to float	          float("3.14") → 3.14
# str()	      Converts to string	      str(100) → "100"
# bool()	  Converts to boolean	      bool(1) → True
# list()	  Converts to list	          list("hello") → ['h','e','l','l','o']
# tuple()	  Converts to tuple	          tuple([1,2,3]) → (1,2,3)
# set()	      Converts to set	          set([1,2,2,3]) → {1,2,3}

# Examples of Type Casting

# String to integer
num_str = "123"
num_int = int(num_str)
print(num_int, type(num_int))  # Output: 123 <class 'int'>

# Integer to float
num_float = float(42)
print(num_float, type(num_float))  # Output: 42.0 <class 'float'>

# Float to string
pi_str = str(3.14159)
print(pi_str, type(pi_str))  # Output: 3.14159 <class 'str'>

# Boolean conversion
print(bool(1))     # True
print(bool(0))     # False
print(bool("Hi"))  # True
print(bool(""))    # False

# Important Note about Typecasting:

# a) not all conversions are possible:
int("hello")  # ValueError: invalid literal for int()

# b) float to integer truncates decimal part:
int(3.99)  # Result is 3 (not rounded)

# c) string must contain valid number for numeric conversion:
int("123")    # Works
int("123abc") # Fails