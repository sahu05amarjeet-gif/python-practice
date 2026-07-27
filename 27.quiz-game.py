#Python quiz game

questions = ("How many elements are in the periodic table?",
             "Which animal lays the largest eggs?", 
             "Which is the most abundant gas in Earth's atmosphere?",
             "How many bones are in the human body?",
             "Which planet in the solar system is the hottest?")
options = (("A. 117", "B. 119", "C. 118", "D. 120"),
           ("A. Whale", "B. Chicken", "C. Ostrich", "D. None of the above"),
           ("A. Nitrogen", "B. Helium", "C. Oxygen", "D. Methane"),
           ("A. 201", "B. 200", "C. 209", "D. 190"),
           ("A. Venus", "B. Jupiter", "C. Earth", "D. Neptune"))
answers = ("C", "C", "A", "B", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if(guess == answers[question_num]):
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------------------------")
print("               RESULT                  ")
print("Answers: ", end="")
for Answer in answers:
    print(Answer, end=" ")
print()

print("Guesses: ", end="")
for Guess in guesses:
    print(Guess, end=" ")
print()

score = int(score/len(questions) * 100)
print(f"Your final score is {score}%")