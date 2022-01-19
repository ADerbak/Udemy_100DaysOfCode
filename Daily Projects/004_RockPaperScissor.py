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

#Write your code below this line 👇
import random

print("Welcome to Rock, Paper, Scissors!")

person = int(input("What do you choose! Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
computer = random.randint(0,2)

commands = [rock, paper, scissors]

print(commands[person])

print(f'Computer chose: \n\n {commands[computer]}')

if person == computer:
    print('Tie!')
elif (person == 0 and computer == 1) or (person == 1 and computer == 2) or (person == 3 and computer == 0):
    print('You lose')
else:
    print('You Win!')