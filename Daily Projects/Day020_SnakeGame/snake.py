from turtle import Turtle

STARTING_POSITIONS = [(0, 0),(-20, 0), (-40, 0)]
MOVE_DISTNACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_segment(i)

    def add_segment(self,position):    
        snake_part = Turtle('square')
        snake_part.penup()
        snake_part.color('white')
        snake_part.goto(position)
        self.segments.append(snake_part)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
           if i > 0:
                x_cor = self.segments[i - 1].xcor()
                y_cor = self.segments[i - 1].ycor()
                self.segments[i].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTNACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    

# for i in range(0, len(snake_parts)):
#     if i == 0:
#         pass
#     else:
#         snake_parts[i].goto(snake_parts[i - 1].xcor() - 20, snake_parts[i - 1].ycor())
    
