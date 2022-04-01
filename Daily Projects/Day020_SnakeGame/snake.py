from turtle import Turtle

STARTING_POSITIONS = [(0, 0),(-20, 0), (-40, 0)]

class Snake:
    
    def __init__(self_):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for i in range(STARTING_POSITIONS):
            snake_part = Turtle('square')
            snake_part.penup()
            snake_part.color('white')
            snake_part.goto(i)
            self.segments.append(snake_part)
    
    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
           if i > 0:
                x_cor = self.segments[i - 1].xcor()
                y_cor = self.segments[i - 1].ycor()
                self.segments[i].goto(x_cor, y_cor)
        self.segments[0].forward(20)


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







for i in range(0, len(snake_parts)):
    if i == 0:
        pass
    else:
        snake_parts[i].goto(snake_parts[i - 1].xcor() - 20, snake_parts[i - 1].ycor())
    
