import turtle
import pandas as pd
import time


# Set up Screen
screen = turtle.Screen()
screen.title('U.S. States Game')

# Add background image shape
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# Read in Pandas file
df = pd.read_csv('50_states.csv')
states = df.state.values
states = states
print(states)


# Make a new Writer
writer = turtle.Turtle()
writer.hideturtle()
answers = []
states_to_learn = []
game = True

game_time = 60
start_time = time.time()

while(game):
    time.sleep(1)

    time_taken = time.time() - start_time
    
    
    # Game Win
    if len(answers) == len(states):
        screen.textinput("Congratulations! You won!","") 
        break 
        
    if time.time() - start_time > game_time: 
        screen.textinput(f"Time Up! final score: {int(round(len(answers)/50))*100}%","")
        states_to_learn = set(states).difference(answers)
        states_to_learn = pd.DataFrame(states_to_learn,columns=['State']).sort_values(by='State').reset_index(drop=True)
        states_to_learn.to_csv("States to learn.csv",index = 'False')
        break

    
    writer.penup()
    # Get Answers from input
    
    
    answer_state = screen.textinput(title=f"{len(answers)}/50 Guess the state! Time Left: {int(round(game_time - time_taken,0))}",prompt="What's another state's name?").title()
    print (answer_state in states) 
    if answer_state in states and answer_state not in answers:
        answers.append(answer_state)
        x,y = int(df[df.state == answer_state].x),int(df[df.state == answer_state].y)
        print(x,y)

        
        writer.setposition(x,y)
        writer.pendown()
        writer.write(answer_state, move=True)
        writer.penup()
        print(answer_state)
    
    screen.update()




# turtle.exitonclick()


