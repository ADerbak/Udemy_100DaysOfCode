from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# Part 1 - Create player, make move from bottom to top of screen and reset.
# Create a turtle player that starts at the bottom of the screen 
# and listen for the "Up" keypress to move the turtle north. 
# If you get stuck, check the video walkthrough in Step 3.

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.start = STARTING_POSITION
        self.move = MOVE_DISTANCE
        self.end = FINISH_LINE_Y
        self.penup()
        self.shape("turtle")
        self.reset_position()
        self.left(90)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(self.start)
        