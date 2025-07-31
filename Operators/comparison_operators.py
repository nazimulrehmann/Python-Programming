# Comparison Operators

# Operator	     Name	                      Example	      Result

#   ==	        Equal	                      5 == 3	      False
#   !=	        Not equal	                  5 != 3	      True
#   >	        Greater than	              5 > 3	          True
#   <	        Less than	                  5 < 3	          False
#   >=	        Greater than or equal to	  5 >= 5	      True
#   <=	        Less than or equal to	      5 <= 3	      False  

# Comparison operators are used to compare values and return a Boolean result (`True` or `False`).
# They are essential for decision-making in programs, such as in `if` statements, loops, and condition checks.


# Detailed Explanation with Examples

# Equal to (`==`)
# Checks if two values are equal.
print(5 == 5)   # True
print("hello" == "hello")  # True
print(3.0 == 3)  # True (Python considers int and float equality)
print([1, 2] == [1, 2])  # True (lists are compared element-wise)


# Not equal to (`!=`)
# Checks if two values are not equal.

print(5 != 3)   # True
print("hi" != "hello")  # True
print(10 != 10.0)  # False (int and float can be equal)

# Greater than (`>`)
# Checks if the left value is greater than the right value.
print(10 > 5)   # True
print("b" > "a")  # True (lexicographical order in strings)
print([3, 4] > [1, 2])  # True (compares element-wise)

# Less than (`<`)**
# Checks if the left value is less than the right value.
print(3 < 7)   # True
print("apple" < "banana")  # True (string comparison)
print([1, 2] < [1, 3])  # True (element-wise comparison)

# Greater than or equal to (`>=`)
# Checks if the left value is greater than or equal to the right value.
print(8 >= 8)   # True
print(10 >= 5)  # True
print("z" >= "a")  # True (strings compared by ASCII values)

# Less than or equal to (`<=`)
# Checks if the left value is less than or equal to the right value
print(4 <= 5)   # True
print(5 <= 5)   # True
print("a" <= "b")  # True

# Chained Comparisons
# Python allows chaining comparison operators for concise checks.
x = 5
print(1 < x < 10)  # True (equivalent to 1 < x and x < 10)
print(3 <= x <= 7)  # True

# Exercises with Solutions

# Exercise 1: Basic Comparisons
a = 10
b = 5
print(a == b)   # False
print(a != b)   # True
print(a > b)    # True
print(b < a)    # True
print(a >= 10)  # True
print(b <= 4)   # False


# Exercise 2: String Comparisons
name1 = "Alice"
name2 = "Bob"
print(name1 == name2)  # False
print(name1 < name2)   # True ('A' comes before 'B' in ASCII)
print(name1 != name2)  # True


# Exercise 3: List Comparisons

list1 = [1, 2, 3]
list2 = [1, 2, 4]
print(list1 == list2)  # False (different elements)
print(list1 < list2)   # True (3 < 4 in element-wise comparison)

# Exercise 4: Chained Comparisons

x = 15
print(10 < x < 20)  # True
print(5 <= x <= 15) # True
print(x == 15 or x > 20)  # True (equivalent to `x == 15 | x > 20`)



# Practical Applications
# Conditional Statements (`if-else`)
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loop Conditions (`while`)
count = 0
while count < 5:
    print(count)
    count += 1

# Sorting & Filtering Data
numbers = [10, 20, 30, 40, 50]
filtered = [x for x in numbers if x > 25]  # [30, 40, 50]

# Final Challenge 

a, b, c = 5, 10, 15
print(a + b == c)      # True (5 + 10 = 15)
print(b * 2 > c)       # True (10 * 2 = 20 > 15)
print(a <= b <= c)     # True (5 ≤ 10 ≤ 15)

# Try these in your Python interpreter and experiment with different values!

# Chaining Comparisons:
# Python allows chaining comparison operators:
# This checks if 5 < 10 and 10 < 15
result = 5 < 10 < 15  # True

# Equivalent to
result = (5 < 10) and (10 < 15)  # True