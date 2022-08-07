from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move = True, align = 'center', font= FONT)
