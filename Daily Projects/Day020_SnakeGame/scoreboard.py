from shutil import move
from turtle import Turtle

SCORE = 0

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.score = 0
    
    def scoreboard(self):
        self.score
        self.font = ('Arial',25,'normal')
        self.color('white')
        self.goto(0, 250)
        self.write(arg = f"Score = {self.score}"
                , move=True
                , align='center'
                , font = self.font )
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.scoreboard()
        
        
        