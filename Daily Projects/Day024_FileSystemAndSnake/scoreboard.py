from shutil import move
from turtle import Turtle

ALIGN = 'center'
FONT = ('Arial',25,'normal')
FILEPATH = './Daily Projects/Day024_FileSystemAndSnake/data.txt'
with open(FILEPATH) as file:
    HIGHSCORE = int(file.read())

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.score = 0
    
    def scoreboard(self):
        self.score
        self.high_score = HIGHSCORE
        self.color('white')
        self.goto(0, 250)
        self.update_scoreboard()
    
    # def update_score(self):
    #     self.clear()
    #     self.score += 1
    #     self.scoreboard()
        
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGN, font = FONT)
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", move = True, align = ALIGN, font= FONT)
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(FILEPATH,mode = 'w') as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        
        
        
        