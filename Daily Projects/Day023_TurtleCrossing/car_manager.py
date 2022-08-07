from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# Part II - Create randomly generated cars
# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis 
# and move to the left edge of the screen. No cars should be generated  in the top and bottom 
# 50px of the screen (think of it as a safe zone for our little turtle). 
# Hint: generate a new car only every 6th time the game loop runs. 
# If you get stuck, check the video walkthrough in Step 4.

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.generate_car(self.number_of_cars)
        self.level = 0
        self.cars = []
        self.number_of_cars = 20
        
        
    def move_car(self):             
        self.goto(self.xcor()+(STARTING_MOVE_DISTANCE+MOVE_INCREMENT*self.level), self.ycor())
        
    def generate_car(self,number_of_cars):
        self.penup()
        self.shape("square")
        self.color(COLORS[random.randint(0,5)])
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(random.randint(-250,250), 400)
        self.cars = self.segments.append(number_of_cars)
    
    def create_car(self):
        for i in self.number_of_cars:
            self.generate_car(i)
        
