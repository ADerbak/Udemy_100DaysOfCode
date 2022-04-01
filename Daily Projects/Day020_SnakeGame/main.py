from turtle import Screen, Turtle
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('--__--__-->~ Snake Game! ~<--__--__--')

snake_counter = 3
snake_parts = []

def move_forwards():
    snake_parts[0].forward(20)

def move_backwards():
    snake_parts[0].backward(0)

def rotate_right():
    snake_parts[0].right(90)
    #snake_parts[0].forward(20)

def rotate_left():
    snake_parts[0].left(90)
    #snake_parts[0].forward(20)



for i in range(snake_counter):
    snake_parts.append(Turtle('square'))
    snake_parts[i].penup()
    snake_parts[i].color('white')


for i in range(0, len(snake_parts)):
    if i == 0:
        pass
    else:
        snake_parts[i].goto(snake_parts[i - 1].xcor() - 20, snake_parts[i - 1].ycor())

game = True

screen.tracer(0)

while game:
    screen.update()
    time.sleep(0.1)
    for i in range(len(snake_parts)-1, 0, -1):
        if i > 0:
            x_cor = snake_parts[i - 1].xcor()
            y_cor = snake_parts[i - 1].ycor()
            snake_parts[i].goto(x_cor, y_cor)
        else:
            pass
    snake_parts[0].forward(20)


    screen.listen()
    screen.onkey(key="d", fun=rotate_right)
    screen.onkey(key="a", fun=rotate_left)








screen.exitonclick()