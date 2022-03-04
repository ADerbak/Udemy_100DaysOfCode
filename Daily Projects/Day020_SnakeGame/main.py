from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('--__--__-->~ Snake Game! ~<--__--__--')

snake_counter = 3
snake_parts = []

for i in range(snake_counter):
    snake_parts.append(Turtle('square'))
    snake_parts[i].penup()
    snake_parts[i].color('white')


# snake_head = Turtle('square')
# snake_head.penup()
# snake_head.color('white')
# snake_body1 = Turtle('square')
# snake_body1.penup()
# snake_body1.color('white')
# snake_body2 = Turtle('square')
# snake_body2.penup()
# snake_body2.color('white')

# snake_parts[1].goto(snake_parts[0].xcor()-20, snake_parts[0].ycor())
# snake_parts[2].goto(snake_parts[1].xcor()-20, snake_parts[1].ycor())

for i in range(0,len(snake_parts)):
    if i == 0:
        pass
    else:
        snake_parts[i].goto(snake_parts[i-1].xcor()-20, snake_parts[i-1].ycor())







screen.exitonclick()