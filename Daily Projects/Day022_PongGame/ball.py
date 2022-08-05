from turtle import Turtle


class Ball(Turtle):
    
    def __iniit__(self):
        super().__init__
        # Ball creation
        self.penup()
        self.shape('circle')
        self.color('white')