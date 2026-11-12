
import random

print("===== ROCK PAPER SCISSORS =====")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("\nChoose rock, paper, scissors (or quit): ").lower()

    if user == "quit":
        print("Game Over!")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You:", user)
    print("Computer:", computer)

    if user == computer:
        print("It's a Draw!")

    elif user == "rock" and computer == "scissors":
        print("You Win!")

    elif user == "paper" and computer == "rock":
        print("You Win!")

    elif user == "scissors" and computer == "paper":
        print("You Win!")

    else:
        print("Computer Wins!")
