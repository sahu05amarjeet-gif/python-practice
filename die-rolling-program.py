#Dice rolling programm made by me first time. 

import random

is_running = True
while is_running:
    user = input("Do you want to roll the dice? (y/n): ").lower()
    if user.lower() == "y":
        print(random.randint(1, 6), random.randint(1,6), sep = ",")
        again = input("Do you want to re roll the dice again?: ").lower()
        if again == "y" or again == "Y":
            print(random.randint(1, 6), random.randint(1,6), sep = ",")
        elif again == "n" or again == "N":
            print("Thankyou for playing this game")
            is_running = False
    else:
        print("Invalid choice")




