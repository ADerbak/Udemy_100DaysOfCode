from turtle import Turtle, Screen

tim = Turtle()
tim.shape('turtle')
tim.color('cyan')

# Challenge 1 - Draw a square
#timmy_the_turtle.forward(100)
# for i in range(0,4):
#     tim.forward(100)
#     tim.left(90)

#Challenge 2 - Draw a dashed line
for i in range(15):
    tim.pendown()
    tim.forward(5)
    tim.penup()
    tim.forward(5)




screen = Screen()
screen.exitonclick()