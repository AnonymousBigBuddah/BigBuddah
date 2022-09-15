import random

# Variables
user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

def WinLose():
    computer_wins = 0
    user_wins = 0
    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
    else:
        print("You lost")
        computer_wins += 1

# Loop
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    WinLose()








print("You won", user_wins,"times.")
print("The computer won", computer_wins, "times.")

print("Shutdown")





# Calculator.
# Countdown Clock and Timer.
# Random Password Generator.
# Random Wikipedia Article.
# Reddit Bot.
# Python Command-Line Application.
# Alarm Clock.
# Tic-Tac-Toe.