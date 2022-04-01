from turtle import Turtle

STARTING_POSITIONS = [(0, 0),(-20, 0), (-40, 0)]
MOVE_DISTNACE = 20

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        
    def create_snake(self):
        for i in STARTING_POSITIONS:
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
        self.segments[0].forward(MOVE_DISTNACE)

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)
    




# for i in range(0, len(snake_parts)):
#     if i == 0:
#         pass
#     else:
#         snake_parts[i].goto(snake_parts[i - 1].xcor() - 20, snake_parts[i - 1].ycor())
    
