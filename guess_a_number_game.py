import random
from colorama import Fore

computer_number = random.randint(1, 100)

while True:
    player_input = input("Guess the number (1-100): ")

    if not player_input.isdigit():
        print("Invalid input. Try again...")
        continue

    player_input = int(player_input)

    if player_input == computer_number:
        print(Fore.BLUE + "You guess the number!")
        break
    elif player_input > computer_number:
        print("too High!")
    else:
        print("Too Low!")
