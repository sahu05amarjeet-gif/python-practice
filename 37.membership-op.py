# word = "APPLE"

# letter = input("Guess a letter in the word: ")

# if letter not in word:
#     print(f"{letter} is not in the word")
# else:
#     print(f"{letter} is in the word")

grades = {"Rock": "A+", "Rohan": "C", "Ram": "B"}

student = input("Enter the name of the student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student}'s name was not found")

email = "nomore@gmail.com"

ask = input("Enter your email: ")

if "@" in ask and "." in ask:
    print("Valid Email")
else:
    print("Invalid Email")

#Membership operators = used to test whether a value or variable is found in sequence.
#                       (string, tuples, sets, or dictionory) in and not in. Returns a boolean


