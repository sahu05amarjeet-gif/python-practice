# Python number guessing game

import random

lowest_num = 1
highest_num = 100
guesses = 0
answer = random.randint(lowest_num, highest_num)
is_Running = True

print("Python Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_Running:
    guess = input("Enter your guess: ")
    if(guess.isdigit()):
        guess = int(guess)
        guesses += 1

        if(guess<lowest_num or guess>highest_num):
            print("That number is out of range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif(guess < answer):
            print("Too Low! Try again!")
        elif(guess>answer):
            print("Too High! Try again")
        elif(guesses == 1):
            print("Congrats! You are one of the luckiest person")
        else:
            print(f"CORRECT! The correct answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_Running = False

    else:
        print("Not a valid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")

