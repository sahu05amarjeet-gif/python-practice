import random
wallet = 100

print("🎲 Welcome to the Dice Betting Arena! 🎲")
print("Rules: Guess if the total of two dice is High (8-12), Low (2-6), or exactly 7.")

while(wallet>0):
    print(f"\n You currently have: ${wallet}")

    bet = input("Enter the bet amount in $ (or 'quit' to exit): ")
    if(bet.lower() == "quit"):
        print("Thanks for playing")
        break
    bet = int(bet)
    if(bet>wallet or bet<=0):
        print("Invalid amount! You can't bet more than you have.")
        continue
    prediction = int(input("Predict your outcome (High/low/7): ")).lower()
    if prediction not in ["high", "low", "7"]:
        print("Invalid choise")
        continue
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = die1 + die2
    print(f"Rolling... 🎲 {die1} and 🎲 {die2} = Total: {die3}")
    