# while loop = execute some code WHILE some conditions remains true

# name = input("Enter your name: ")
# 
# while (name == ""):
    # print("You did not write your name.")
    # name = input("Enter your name: ")  # -> this line prevents infinte loop
# print(f"Hello, {name}")


# age = int(input("Enter your age: "))

# while (age<0):
#     print("Your age cannot be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} old")

food = input("Enter the food you like: ")

while not (food=="q"):
    print(f"You like {food}")
    food = input("Enter another food you like: ")

print("bye")
