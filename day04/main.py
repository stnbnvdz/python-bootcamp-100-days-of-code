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

print("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")

# Mapping the user input to the corresponding choice
user_choice = int(input())

choices = ["rock", "paper", "scissors"]
user_choice_name = choices[user_choice]

import random

computer_choice = random.randint(0, 2)
computer_choice_name = choices[computer_choice]

print(f"\nYou chose: {user_choice_name}")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

print(f"\nComputer chose: {computer_choice_name}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

# Determine the winner
if (user_choice == 0 and computer_choice == 2) or \
   (user_choice == 1 and computer_choice == 0) or \
   (user_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("Computer wins!")
