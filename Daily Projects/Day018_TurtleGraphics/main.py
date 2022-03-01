from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('cyan')

# Challenge 1 - Draw a square
#timmy_the_turtle.forward(100)
# for i in range(0,4):
#     tim.forward(100)
#     tim.left(90)

# Challenge 2 - Draw a dashed line
# for i in range(15):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

# Challenge 3 - Draw different shapes with random colors

color = ['red','blue','green','cyan','black']
# for i in range(3,10):
#     total = 360
#     angle = total/i
#     tim.color(random.choice(color))
#     for i in range(i):
#         tim.forward(50)
#         tim.right(angle)


# Challenge 4 - Create a random walk

angle = [90,270]
tim.width(10)
for i in range(100):
    tim.color(random.choice(color))
    tim.forward(50)
    tim.left(random.choice(angle))
tim.forward(50)

screen = Screen()
screen.exitonclick()