from turtle import Screen, Turtle




screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

right_paddle = Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_len=100, stretch_wid=20)
right_paddle.goto(x=350,y=0)
right_paddle.onclick()

screen.exitonclick()