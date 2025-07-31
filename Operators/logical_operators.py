# Logical Operators
# Logical operators are used to combine conditional statements.

#  Operator	       Description	                                       Example
#    and	       True if both statements are true     	         x < 5 and x < 10
#    or	           True if at least one statement is true	         x < 5 or x < 4
#    not	       Reverse the result (False becomes True, etc.)	 not(x < 5 and x < 10)

# Logical operators (`and`, `or`, `not`) are used to combine or modify conditions in Python.
# They are often used with `if`, `elif`, and `else` statements.


# Combining with `if`, `elif`, `else`
# Example 1: `and` (Both Conditions True)
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter!")
else:
    print("Sorry, you can't enter.")
# `You can enter!` (because both conditions are `True`)

#Example 2: `or` (At Least One Condition True)

weather = "rainy"
umbrella = False

if weather == "sunny" or umbrella:
    print("You won't get wet!")
else:
    print("Bring an umbrella!")
 
# `Bring an umbrella!` (because neither condition is `True`)

#Example 3: `not` (Reverse Condition)
logged_in = False

if not logged_in:
    print("Please log in first.")
else:
    print("Welcome!")

# `Please log in first.` (because `not False` → `True`)

# Combining with Other Operators
# Example 4: `and` + `or`
temperature = 28
is_summer = True

if temperature > 30 or (is_summer and temperature > 25):
    print("It's hot!")
else:
    print("It's not too hot.")

# `It's hot!` (because `is_summer and temperature > 25` is `True`)

# Example 5: `not` with `in` (Check if Item is NOT in List)
fruits = ["apple", "banana", "orange"]

if "mango" not in fruits:
    print("Mango is missing!")
else:
    print("Mango is available.")

  
# `Mango is missing!` (because `"mango"` is not in `fruits`)


# 4. Exercises
# Exercise 1: Username & Password Check

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Wrong username or password.")


# Exercise 2: Discount Eligibility

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if age < 18 or is_student:
    print("You get a discount!")
else:
    print("No discount for you.")


# Exercise 3: Number Checker

num = int(input("Enter a number: "))

if num > 0 and num % 2 == 0:
    print("Positive and even!")
elif num > 0 and num % 2 != 0:
    print("Positive and odd!")
elif num < 0:
    print("Negative number!")
else:
    print("It's zero!")

# Exercise 4: Movie Ticket Pricing

age = int(input("Enter your age: "))
is_vip = input("Are you a VIP? (yes/no): ").lower() == "yes"

if age < 5:
    price = 0
elif age <= 12 or is_vip:
    price = 10
else:
    price = 15

print(f"Your ticket price is ${price}")

