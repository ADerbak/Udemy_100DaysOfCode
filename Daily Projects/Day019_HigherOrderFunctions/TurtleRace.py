from turtle import Turtle, Screen


screen = Screen()
screen.setup(height=400, width=500)

bet = screen.textinput(title="TURTLE RACE!", prompt = "Which turtle will win the race? Please enter a color: ")
print(bet)

colors = ['red', 'orange', 'gold', 'green', 'blue', 'purple']
turtles = []
increment = 0

for i in range(0,len(colors)):
    turtles.append(Turtle(shape='turtle'))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x = -230, y = -100 + increment)
    increment += 40


















screen.exitonclick()