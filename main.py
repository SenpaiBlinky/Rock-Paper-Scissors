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

import random

user = int(input("What do you choose? Type 0 for 'Rock', 1 for 'Paper', 2 for 'Scissors', "))

options = [rock, paper, scissors]
options_word = ["rock", "paper", "scissors"]

comp = random.randint(0,2)

print(f"you chose {options_word[user]} {options[user]}")
print(f"computer chose {options_word[comp]} {options[comp]}")

if comp == 0:
  if user == 0:
    print("You tied")
  if user == 1:
    print("You win")
  else:
    print("You lose")
if comp == 1:
  if user == 0:
    print("You lose")
  if user == 1:
    print("You tie")
  else:
    print("You win")
if comp == 2:
  if user == 0:
    print("You win")
  if user == 1:
    print("You lose")
  else:
    print("You tie")
