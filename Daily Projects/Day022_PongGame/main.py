from turtle import Screen, Turtle, ycor
from paddle import Paddle
from ball import Ball
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



# x,y = 0,0

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    
    
    #while (ball.xcor()<400 and ball.xcor() >-400):
        
    # Determine if ball hits a paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_direction *= -1
            
       
    
    
    

screen.exitonclick()