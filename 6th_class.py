# ROCK PAPER SCISSOR GAME
# rock - fist
# paper - flat hand
# scissors - index and middle finger
# import random

# rock beats scissors
# scissors beats paper
# paper beats rock

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

welcome = '''
__________               __         __________                                 _________      .__                                  
\______   \ ____   ____ |  | __     \______   \_____  ______   ___________    /   _____/ ____ |__| ______ _________________  ______
 |       _//  _ \_/ ___\|  |/ /      |     ___/\__  \ \____ \_/ __ \_  __ \   \_____  \_/ ___\|  |/  ___//  ___/  _ \_  __ \/  ___/
 |    |   (  <_> )  \___|    <       |    |     / __ \|  |_> >  ___/|  | \/   /        \  \___|  |\___ \ \___ (  <_> )  | \/\___ \ 
 |____|_  /\____/ \___  >__|_ \ /\   |____|    (____  /   __/ \___  >__| /\  /_______  /\___  >__/____  >____  >____/|__|  /____  >
        \/            \/     \/ )/                  \/|__|        \/     )/          \/     \/        \/     \/                 \/ 
'''

# print(welcome)
# game_images = [rock, paper, scissors]
# game_choices = ["rock", "paper", "scissors"]
# user_choice = input("Please enter your choice. (Rock, Paper, Scissors)").lower()
# computer_choice = random.choice(game_choices)
# print(f"You chose: {user_choice.upper()} and computer chose: {computer_choice.upper()} ")
# if user_choice == "rock" and computer_choice == "scissors":
#     print("You win!")
#     print(rock)
# elif computer_choice == "rock" and user_choice == "scissors":
#     print("Computer wins. You lose!")
# elif user_choice == "scissors" and computer_choice == "paper":
#     print(scissors)
#     print("You win!")
# elif computer_choice == "scissors" and user_choice == "paper":
#     print("Computer wins. You lose!")
# elif user_choice == "paper" and computer_choice == "rock":
#     print("You win!")
# elif computer_choice == "paper" and user_choice == "rock":
#     print("Computer wins. You lose!")
# elif computer_choice == user_choice:
#     print("Its a tie.")
# else:
#     print("You chose an invalid move. You Lose!")

# name = "AsAd ullah"
# print(name.upper())
# print(name.lower())
# print(name.title())


# rock - 0, paper - 1, scissors - 2
# 0 beats 2
# 2 beats 1
# 1 beats 0
import random

game_images = [rock, paper, scissors]
print(welcome)
user_choice = int(input("Please enter your choice. Type 0 for Rock, 1 for Paper, 2 for Scissors."))


if user_choice >=0 and user_choice <= 2:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])
    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You Win!")
else:
    print("You chose an invalid number. You lose!")


