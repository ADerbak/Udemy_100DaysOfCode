#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = '''
  ________                             ___________.__              _______               ___.                  
 /  _____/ __ __  ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________  
/   \  ___|  |  \/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \ 
\    \_\  \  |  |  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ 
 \______  /____/ \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|    
        \/           \/     \/     \/                  \/     \/          \/            \/    \/     \/        

'''
import random

number  = random.randint(1,100)
guesses = 0
print(logo,'\n',f'''
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
Pssst, the correct answer is {number}
''')

level = input("Choose a difficulty. Type 'easy' or 'hard': ")


if level == 'hard':
  guesses = 5
else:
  guesses = 10


def game():
  global guesses
  global number

  while guesses > 0:
    user_number = int(input("Make a guess: "))
    if user_number == number:
      print(f"You got it! the answer was {number}")
      break
    else:
      if user_number > number:
        print("Too High.")
      else:
        print("Too low.")
        guesses -= 1
        
    if guesses > 0 :
      print(f"Guess again.\nYou have {guesses} guesses remaining")
    else:
      print('You have ran out of guesses. You lose.')

game()