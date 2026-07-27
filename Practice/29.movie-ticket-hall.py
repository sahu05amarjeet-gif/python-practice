menu = {"pizza": 3.00,              # -> Dictionary
        "burger": 4.50,
        "nachos": 3.25,
        "popcorn": 6.95,
        "fries": 2.25,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []  # -- > List
total = 0   # -> count the total, integer.
print("-------------MENU--------------)")
for keys,values in menu.items():            # -> To show all the items in the menu
    print(f"{keys:10}: ${values:.2f}")
print("--------------------------------")

while True:
    food = input("Enter the food you want (q to quit): ").lower()
    if (food == "q"):
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------ YOUR ORDER -----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Your Total: ${total:.2f}")