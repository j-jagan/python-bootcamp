import random

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
game = [rock, paper, scissors]

un = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if un >= 0 and un <= 2:
    print(game[un])
    computer = random.randint(0, 2)
    print("Computer chose: \n")
    print(game[computer])
    if un == computer:
        print("It's a draw")
    elif un ==0 and computer == 2:
        print("You win!")
    elif un ==2 and computer == 0:
        print("You lose!")
    elif un < computer:
        print("You win!")
    elif computer < un:
        print("You lose!")
else:
    print("You must enter a number between 0 to 2.")
