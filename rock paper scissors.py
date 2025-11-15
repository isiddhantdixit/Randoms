import random

choices = ["rock", "paper", "scissor"]

while True:
    print("\n--- Rock Paper Scissor ---")
    user = input("Enter rock / paper / scissor (or 'quit' to stop): ").lower()

    if user == "quit":
        print("Game ended. Goodbye!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose :", user)
    print("Computer :", computer)

    if user == computer:
        print("Result: It's a tie!")
    elif (user == "rock" and computer == "scissor") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissor" and computer == "paper"):
        print("Result: You win!")
    else:
        print("Result: You lose!")
