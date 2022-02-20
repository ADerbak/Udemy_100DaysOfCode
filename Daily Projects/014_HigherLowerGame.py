# All of this was done from scratch :-)

from game_data import data
#import art
#from replit import clear
import random


# Create a function to handle selecting records from our data (list)
def selection():
  ''' Return a dictionary object from our list of celebrities '''
  # Pick an intial random number
  selection = random.randint(0,len(data)-1)

  # Check to see if it has already been selected
  while selection in selections:
    selection = random.randint(0,len(data)-1)
    
  # Bring back data for new integer
  selections.append(selection)
  compare_dict = data[selection]
  
  return compare_dict

# Create a game variable
gamePlay = True

# Get a list of selections
selections = []

# Set up initial score
score = 0

# Set up initial selection
compare_A = selection()

# Start Game Play
while gamePlay:

  compare_B = selection()  

  # Show logo
  #print(art.logo)
  if score > 0:
    print(f"You're right! Current score: {score}.")

  # Show results
  print(f'Compare A: {compare_A["name"]}, a {compare_A["description"]}, from {compare_A["country"]}')
  #print(art.vs)
  print("VERSUS")
  print(f'Compare B: {compare_B["name"]}, a {compare_B["description"]}, from {compare_B["country"]}')

  guess = input("Who has more followers? Type 'A' or 'B': ").upper()

  if guess == 'A' and compare_A["follower_count"] > compare_B["follower_count"]:
    score += 1
    #clear()
  elif guess == 'B' and compare_A["follower_count"] < compare_B["follower_count"]:
    score += 1
    compare_A = compare_B
    #clear()
  else:
    gamePlay = False
    #clear()

#print(art.logo)
print(f"Sorry, that's wrong. Final Score: {score}.")