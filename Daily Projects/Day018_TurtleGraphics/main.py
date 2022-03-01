# from turtle import Turtle, Screen, colormode
import turtle
import turtle as t
import random

canvasColor = "white"

tim = t.Turtle()
#tim.shape('turtle')
tim.color(canvasColor)

# Challenge 1 - Draw a square
# timmy_the_turtle.forward(100)
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

color = ['red', 'blue', 'green', 'cyan', 'black']
# for i in range(3,10):
#     total = 360
#     angle = total/i
#     tim.color(random.choice(color))
#     for i in range(i):
#         tim.forward(50)
#         tim.right(angle)


# Challenge 4 - Create a random walk
#
# angle = [0, 90, 180, 270]
# #tim.width(10)
# tim.speed("fastest")
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# for i in range(200):
#     tim.pencolor(random_color())
#     tim.forward(50)
#     tim.setheading(random.choice(angle))
# tim.forward(50)



# Challenge 5 - Make a spirograph

# radius = 100
# turn = 5
# turns = int(360/turn)
#
# for i in range(turns):
#     tim.pencolor(random_color())
#     tim.circle(radius)
#     tim.left(turn)

    # Another way:
    # current_heading = tim.heading()
    # tim.setheading(current_heading + 10)

# Final Project

# 10 x 10 Dots, radius = 20, separated by 50 paces
t.colormode(255)
tim.speed("fastest")

hirstColors =[
    (245, 243, 238),
    (246, 242, 244),
    (202, 164, 110),
    (240, 245, 241),
    (236, 239, 243),
    (149, 75, 50),
    (222, 201, 136),
    (53, 93, 123),
    (170, 154, 41),
    (138, 31, 20),
    (134, 163, 184),
    (197, 92, 73),
    (47, 121, 86),
    (73, 43, 35),
    (145, 178, 149),
    (14, 98, 70),
    (232, 176, 165),
    (160, 142, 158),
    (54, 45, 50),
    (101, 75, 77),
    (183, 205, 171),
    (36, 60, 74),
    (19, 86, 89),
    (82, 148, 129),
    (147, 17, 19),
    (27, 68, 102),
    (12, 70, 64),
    (107, 127, 153),
    (176, 192, 208),
    (168, 99, 102)]

# Set initial starting point
tim.up()
tim.left(270)
tim.forward(250)
tim.left(270)
tim.forward(250)
tim.left(180)

# Draw a series of circles (dots)
radius = 20

for i in range(10):

    # Draw a row of dots
    for i in range(10):
        tim.down()
        # You can also use dot method; I did both!

        # Dot Method - this more closely matches the videos
        tim.pen(pencolor=hirstColors[random.randint(0,len(hirstColors)-1)])
        tim.dot(size = radius  )

        # Circle Method
        #tim.fillcolor(hirstColors[random.randint(0,len(hirstColors)-1)])
        #tim.begin_fill()
        #tim.circle(radius = radius)
        #tim.end_fill()
        tim.up()
        tim.forward(50)

    # Move up and to the left
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

tim.hideturtle()

screen = t.Screen()
screen.bgcolor(canvasColor)
screen.exitonclick()
