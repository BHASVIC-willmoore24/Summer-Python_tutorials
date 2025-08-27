import random

def game_win(player_choice, computer_choice):
    if player_choice == computer_choice:
        print("Win")
    else:
        print("Lose")


num = random.randint(1, 2)
choice = 0
choice = int(input("Guess a number, 1 or 2: "))
game_win(choice, num)





