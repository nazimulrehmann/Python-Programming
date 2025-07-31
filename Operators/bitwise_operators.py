# Bitwise Operators in Python

# Bitwise operators are used to perform operations on individual bits of integers. 
# These operators work directly on the binary representations of numbers. 
# Understanding bitwise operations is essential for low-level programming, cryptography, and optimizing certain algorithms.

# How Bitwise Operators Work

# Before diving into the operators, it's important to understand how Python represents integers in binary:
# - Integers are stored in memory as binary numbers (base 2)
# - For positive numbers, the binary representation is straightforward
# - Negative numbers are represented using two's complement notation

# Bitwise Operators in Python

# Bitwise AND (`&`)
# Performs a logical AND operation on each pair of corresponding bits. Returns `1` only if both bits are `1`.

a = 10    # 1010 in binary
b = 4     # 0100 in binary
result = a & b
print(result)  # Output: 0 (0000 in binary)

# Breakdown:
#   1010 (10)
# & 0100 (4)
#   ----
#   0000 (0)


# Bitwise OR (`|`)
# Performs a logical OR operation on each pair of corresponding bits. Returns `1` if at least one of the bits is `1`.

a = 10    # 1010
b = 4     # 0100
result = a | b
print(result)  # Output: 14 (1110)

# Breakdown:
#   1010 (10)
# | 0100 (4)
#   ----
#   1110 (14)

# Bitwise XOR (`^`)
# Performs an exclusive OR operation. Returns `1` if the bits are different, `0` if they're the same.

a = 10    # 1010
b = 4     # 0100
result = a ^ b
print(result)  # Output: 14 (1110)

# Breakdown:
#   1010 (10)
# ^ 0100 (4)
#   ----
#   1110 (14)

a = 10    # 1010
b = 11    # 1011
result = a ^ b
print(result)  # Output: 1 (0001)

# Bitwise NOT (`~`)
# Flips all the bits of the number. This is equivalent to `-(x + 1)` because Python uses two's complement for negative numbers.

a = 10    # ...0001010 (assuming 32-bit)
result = ~a
print(result)  # Output: -11

# Explanation:
# Original: 00000000 00000000 00000000 00001010 (10)
# After ~:  11111111 11111111 11111111 11110101 (-11 in two's complement)

# Left Shift (`<<`)
# Shifts the bits of the number to the left by the specified number of positions. This is equivalent to multiplying by `2^n`.

a = 5     # 0101
result = a << 1
print(result)  # Output: 10 (1010)

# Breakdown:
# 0101 (5) shifted left by 1 becomes 1010 (10)
# Equivalent to 5 * 2^1 = 10


# Right Shift (`>>`)
# Shifts the bits of the number to the right by the specified number of positions. This is equivalent to integer division by `2^n`.

a = 10    # 1010
result = a >> 1
print(result)  # Output: 5 (0101)

# Breakdown:
# 1010 (10) shifted right by 1 becomes 0101 (5)
# Equivalent to 10 // 2^1 = 5


# Practical Applications of Bitwise Operators

# Checking if a number is even or odd
num = 7
if num & 1:
    print("Odd")  # Output: Odd
else:
    print("Even")


# Swapping two numbers without temporary variable
x = 5
y = 3

x = x ^ y
y = x ^ y
x = x ^ y

print(x, y)  # Output: 3 5


# Setting and clearing specific bits.
# Set the 3rd bit (0-indexed from right) of a number
num = 4      # 0100
mask = 1 << 2  # 0100
num |= mask
print(num)   # Output: 4 (unchanged since bit was already set)

# Clear the 2nd bit
num = 6      # 0110
mask = ~(1 << 1)  # 1101
num &= mask
print(num)   # Output: 4 (0100)

# Checking if the nth bit is set

def is_bit_set(num, n):
    return num & (1 << n) != 0

print(is_bit_set(5, 0))  # True (5 is 0101, bit 0 is 1)
print(is_bit_set(5, 1))  # False (bit 1 is 0)

# Counting set bits (Hamming weight)

def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

print(count_set_bits(7))  # 3 (0111 has 3 set bits)


# Important Notes

#  **Bitwise operators only work on integers** - Using them with floats will raise a TypeError.
#  **Negative numbers** - Bitwise operations on negative numbers work with their two's complement representation.
# **Operator precedence** - Bitwise operators have lower precedence than arithmetic operators but higher than comparison operators.
# **Bit length** - Python integers can be arbitrarily large, so bitwise operations don't have overflow issues like in some other languages.

'''
Performance Considerations

Bitwise operations are generally very fast because they map directly to processor instructions.
They're often used in performance-critical code, such as:

- Cryptography algorithms
- Compression algorithms
- Network protocols
- Graphics programming
- Embedded systems programming
'''