from turtle import Turtle

class Paddle:
    
    def __init__(self, coord):
        x, y = coord
        self = Turtle()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        
        self.goto(x=x,y=y)
        
    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)
    
    def go_down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
