from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def rotate_right():
    tim.right(10)

def rotate_left():
    tim.left(10)

def clear_screen():
    tim.clear()
    tim.reset()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=rotate_right)
screen.onkey(key="a", fun=rotate_left)
screen.onkey(key="space", fun=clear_screen)
screen.exitonclick()
