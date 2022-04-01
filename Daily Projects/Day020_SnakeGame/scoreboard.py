from shutil import move
from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial',25,'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.score = 0
    
    def scoreboard(self):
        self.score
        self.color('white')
        self.goto(0, 250)
        self.write(arg = f"Score = {self.score}"
                , move=True
                , align= ALIGN
                , font = FONT )
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move = True, align = ALIGN, font= FONT)
        
        
        