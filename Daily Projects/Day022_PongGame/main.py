from turtle import Screen, Turtle
from paddle import Paddle



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
# screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
# paddle = Turtle()
# paddle.penup()
# paddle.shape("square")
# paddle.color("white")
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.goto(x=350,y=0)


# def go_up():
#     new_y = paddle.ycor()+20
#     paddle.goto(paddle.xcor(), new_y)
    
# def go_down():
#     new_y = paddle.ycor()-20
#     paddle.goto(paddle.xcor(), new_y)



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

# game_is_on = True

# while game_is_on:
# screen.update()


screen.exitonclick()