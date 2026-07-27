# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string.

name = input("Please enter your first name here: ")
middle_name = input("Please enter your middle name here: ")
last_name = input("Please enter your last name here: ")
age = int(input("Enter your age: "))

age = age +1 

print(f"Your full name is {name} {middle_name} {last_name}")
print("Happy Birthday")
print(f"Your age is {age}")

# What is f-string? -> used for inserting variables in the strings.
# strings cannot be used directly with arithmetic expressions.