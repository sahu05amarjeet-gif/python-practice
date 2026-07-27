positive = 0
negative = 0
zero = 0

while True:
    user = input("Enter the number +ve, -ve, or zero (q) to exit: ")
    if user == "q":
        break
    num = int(user)
    if num > 0:
        print("Positive number")
        positive += 1
    elif num < 0:
        print("Negative Number")
        negative += 1
    elif num == 0:
        print("Zero")
        zero += 1
    else:
        pass
print(f"You entered: Positive: {positive}, Negative: {negative}, Zero: {zero}")