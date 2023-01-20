import turtle
import pandas as pd


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
print(states)


# Make a new Writer
writer = turtle.Turtle()
writer.hideturtle()
answers = []

game = True

# while(game):
writer.penup()
# Get Answers from input
answer_state = screen.textinput(title=f"{len(answers)}/50 Guess the state",prompt="What's another state's name?").title()
print (answer_state in states) 
if answer_state in states and answer_state not in answers:
    answers.append(answer_state)
    x,y = int(df[df.state == answer_state].x),int(df[df.state == answer_state].y)
    print(x,y)

    
    writer.setposition(x,y)
    writer.pendown()
    turtle.write(answer_state, move=True)
    writer.penup()
    # print(answer_state)




turtle.exitonclick()


