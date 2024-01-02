from art import *
import random

print('''
*********************************************
****Welcome to Rock, Paper and Scissors!!****
*********************************************
''')

game_images = [rock, paper, scissors]
game_options = ["Rock", "Paper", "Scissors"]
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if player_choice < 3:
    print("Player chose : " + game_options[player_choice])

if player_choice < 3:
    print(game_images[int(player_choice)])
computer_choice = random.randint(0, 2)
print("Computer chose : " + game_options[computer_choice])
print(game_images[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("Invalid Option")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice == computer_choice:
    print("Its a Draw!")
elif player_choice > computer_choice:
    print("You win!")
print("Thank you for playing this game!!!")
