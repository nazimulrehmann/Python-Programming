# Operator Precedence in Python (Detailed Summary)
# Operator precedence determines the order in which operations are evaluated in an expression.
# Python follows a specific hierarchy when evaluating expressions with multiple operators.


#      Precedence                                                    Operator Type                              Operators  Example 

#  1)  Parentheses                                                      `( )`                                      `(2 + 3) * 4` 
#  2)  Exponentiation                                                   `**`                                       `2 ** 3` (8) 
#  3)  Bitwise NOT, Unary +/-                                           `~ + -`                                    `-5`, `~x` 
#  4)  Multiplication, Division, Floor Div, Modulo                      `* / // %`                                 `10 / 2` (5.0) 
#  5)  Addition, Subtraction                                            `+ -`                                      `3 + 5` (8) 
#  6)  Bitwise Shifts                                                   `<< >>`                                    `4 << 1` (8) 
#  7)  Bitwise AND                                                      `&`                                        `5 & 3` (1) 
#  8)  Bitwise XOR                                                      `^`                                        `5 ^ 3` (6) 
#  9)  Bitwise OR                                                       `\ `                                       `5 \| 3` (7) 
# 10)  Comparison Operators                                             `== != > < >= <=`                          `x > 5` 
# 11)  Identity Operators                                               `is`, `is not`                             `x is None` 
# 12)  Membership Operators                                             `in`, `not in`                             `"a" in "abc"` 
# 13)  Logical NOT                                                      `not`                                      `not True` (False) 
# 14)  Logical AND                                                      `and`                                      `x > 0 and x < 10` 
# 15)  Logical OR                                                       `or`                                       `x == 5 or x == 10` 
# 16)  Assignment Operators                                             `= += -= *= /=`                            `x = 5` 


# Key Rules

# 1)  Parentheses `( )` 
# Have the highest precedence and force evaluation first.

print((2 + 3) * 4)  # 20 (instead of 2 + (3 * 4) = 14)

# 2) Exponentiation (`**`)
# is evaluated before multiplication/division.

print(2 ** 3 * 2)  # 16 (not 64)

# 3) Unary operators (`+`, `-`, `~`) come next.

print(-3 ** 2)  # -9 (not 9, because exponentiation comes first)

# 4) Multiplication/Division have higher precedence than Addition/Subtraction.

print(3 + 5 * 2)  # 13 (not 16)

# 5) Comparison operators (`==`, `!=`, `>`, `<`) are evaluated before logical operators (`and`, `or`).

print(5 > 3 and 2 < 4)  # True (comparisons evaluated first)

# 6) nLogical `not`** has higher precedence than `and` and `or`.

print(not False and True)  # True (not evaluated first)

# 7) Assignment operators (`=`, `+=`) have the lowest precedence.

x = 5 + 3 * 2  # x = 11 (not 16)




# 3. Associativity (When Precedence is Equal)
# Most operators evaluate left-to-right

print(10 / 2 * 3)  # 15.0 (left-to-right)

# Exponentiation (`**`) is right-associative:

print(2 ** 3 ** 2)  # 512 (not 64, because 3 ** 2 is evaluated first)

# Common Mistakes & Fixes
# Mistake: Ignoring precedence in arithmetic

result = 5 + 10 / 2  # 10.0 (not 7.5)

# Fix:Use parentheses for clarity:

result = (5 + 10) / 2  # 7.5


# Mistake:Misusing logical operators

# if x > 5 and x < 10 or x == 0:  # Ambiguous
# Fix: Explicitly group conditions:
# if (x > 5 and x < 10) or x == 0:  # Clearer




# Exercises
# Exercise 1: Predict the Output

print(3 * 4 + 5 ** 2)  # What's the result?

# Answer:`37` (because `5 ** 2 = 25` is evaluated first, then `3 * 4 = 12`, then `12 + 25 = 37`)

# Exercise 2: Correct the Expression**

x = 10
y = 5
z = x / y + 2 ** 3  # What's the value of z?

# Answer: `10.0` (because `2 ** 3 = 8` and `x / y = 2.0`, then `2.0 + 8 = 10.0`)

# Exercise 3: Parentheses Matter**

a = 5
b = 2
c = (a + b) * 2  # What's c?

# Answer: `14` (because `a + b = 7`, then `7 * 2 = 14`)