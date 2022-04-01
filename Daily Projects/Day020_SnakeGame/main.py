from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('--__--__-->~ Snake Game! ~<--__--__--')
screen.tracer(0)

snake = Snake()


# for i in range(0, len(snake_parts)):
#     if i == 0:
#         pass
#     else:
#         snake_parts[i].goto(snake_parts[i - 1].xcor() - 20, snake_parts[i - 1].ycor())

game = True



while game:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()