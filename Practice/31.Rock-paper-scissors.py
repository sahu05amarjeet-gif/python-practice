# Rock, paper, scissors game

import random

options = ("rock", "paper", "scissor")
# score = 0
playing = True
 
while playing:
    player = None
    computer = random.choice(options)
    score = 0
    while player not in options:
        player = input("Enter (rock, paper, scissor): ")
    print(f"You: {player}")
    print(f"Computer: {computer}")

    if(player == computer):
        print("It's a tie!")
    elif(player == "rock" and computer == "scissor"):
        print("You win!")
        score += 1
    elif(player == "paper" and computer == "rock"):
        print("You win!")
        score += 1
    elif(player == "scissor" and computer == "paper"):
        print("You win!")
        score += 1
    else:
        print("You lose!")

    if not input("Do you want to play again? (y/n): ").lower() == "y":
        playing = False

print("Thanks for playing!")
print(f"Your score is: {score}")
