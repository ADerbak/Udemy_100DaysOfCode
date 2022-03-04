import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400, width=500)

bet = screen.textinput(title="TURTLE RACE!", prompt = "Which turtle will win the race? Please enter a color: ")


colors = ['red', 'orange', 'gold', 'green', 'blue', 'purple']
turtles = []
increment = 0

is_race_on = False

for i in range(0,len(colors)):
    turtles.append(Turtle(shape='turtle'))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x = -230, y = -100 + increment)
    increment += 40

if bet:
    is_race_on = True

winner = ''

while is_race_on:
    random_distance = random.randint(0,10)
    turtles[random.randint(0,len(turtles)-1)].forward((random_distance))
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = str(turtle.color()[0])
            if winner == bet:
                print(f"Congratulations! The {winner} turtle won!")
            else:
                print(f"You lost! The {winner} turtle won the race.")




screen.bye()
#screen.exitonclick()











