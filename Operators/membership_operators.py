# Membership Operators in Python (`in` and `not in`)
# Membership operators are used to test whether a value exists within a sequence
# (like strings, lists, tuples, sets, or dictionaries). They return `True` or `False`.

# Membership Operators
# Operator        Description                                                    Example 

#  `in`        Returns `True` if a value exists in a sequence                    `"a" in "apple"` → `True` 
# `not in`     Returns `True` if a value **does not** exist in a sequence         `10 not in [1, 2, 3]` → `True` 

# A) `in` Operator
# Checks if a value is present in a sequence.

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # True
print("mango" in fruits)   # False


# B) `not in` Operator
# Checks if a value is not present in a sequence.

numbers = [1, 2, 3, 4, 5]
print(6 not in numbers)  # True
print(3 not in numbers)  # False



# Use Cases
# A) With Strings
# Checks for substrings:

text = "Hello, World!"
print("Hello" in text)    # True
print("Python" not in text)  # True

# B) With Lists, Tuples, Sets
# Checks for elements:

my_list = [10, 20, 30]
print(20 in my_list)      # True
print(40 not in my_list)  # True

# C) With Dictionaries
# Checks for keys (not values):

person = {"name": "Alice", "age": 25}
print("name" in person)      # True (checks keys)
print("Alice" in person)     # False (does not check values)


# Practical Examples with `if-else`
# Example 1: Checking Username Availability

usernames = ["alice", "bob", "charlie"]
new_user = input("Enter a username: ")

if new_user in usernames:
    print("Username already taken!")
else:
    print("Username available.")


# Example 2: Password Strength Check

password = input("Enter password: ")
weak_words = ["password", "123456", "admin"]

if password in weak_words:
    print("Your password is too weak!")
else:
    print("Password accepted.")


# Example 3: Vowel Checker

char = input("Enter a letter: ")
vowels = "aeiouAEIOU"

if char in vowels:
    print("It's a vowel!")
else:
    print("Not a vowel.")


# Example 4: Checking for Restricted Words

message = input("Enter your message: ")
banned_words = ["spam", "ad", "scam"]

if any(word in message for word in banned_words):
    print("Message contains banned words!")
else:
    print("Message approved.")


# Exercises
# Exercise 1: Check if a Number is in a List

numbers = [5, 10, 15, 20]
num = int(input("Enter a number: "))

if num in numbers:
    print(f"{num} is in the list!")
else:
    print(f"{num} is not in the list.")


# Exercise 2: Username Validation

existing_users = ["alice", "bob", "eve"]
new_user = input("Choose a username: ")

if new_user not in existing_users:
    print("Username available!")
else:
    print("Username already taken.")


# Exercise 3: Word Search in a Sentence

sentence = "The quick brown fox jumps over the lazy dog"
word = input("Enter a word to search: ")

if word in sentence:
    print(f"'{word}' is in the sentence.")
else:
    print(f"'{word}' is not found.")