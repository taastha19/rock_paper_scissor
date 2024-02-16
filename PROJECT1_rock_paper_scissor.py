# RULES
'''
1. Rock win against Scissors             0    ->    Rock
2. Scissors win againt Paper             1    ->    Paper
3. Paper win against Rock                2    ->    Scissors
'''

import random

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

images=[Rock,Paper,Scissors]
user_choice=int(input('Enter your choice(0 for Rock, 1 for Paper, 2 for Scissor) : '))
if user_choice>2 or user_choice<0:
    print('You entered a invalid Number, You Lose!')
else:
    print('\n','You choose : ')
    print(images[user_choice])
    comp_choice=random.randint(0,2)
    print('\n','Computer choose : ')
    print(images[comp_choice])

    if comp_choice==user_choice:
        print("It's a Draw!")
    elif comp_choice==0 and user_choice==2:
        print('You Loose!')
    elif user_choice==0 and comp_choice==2:
        print('You Win!')
    elif comp_choice>user_choice:
        print('You Loose!')
    elif user_choice>comp_choice:
        print('You Win!')

















































