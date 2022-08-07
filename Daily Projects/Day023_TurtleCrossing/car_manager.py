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
        self.hideturtle()
        # self.generate_car(self.number_of_cars)
        self.level = 0
        self.all_cars = []
        
        # self.number_of_cars = 20
        
        
    def move_car(self):  
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT*self.level))
        
    # def generate_car(self,number_of_cars):
    #     self.penup()
    #     self.shape("square")
    #     self.color(COLORS[random.randint(0,5)])
    #     self.shapesize(stretch_len=2, stretch_wid=1)
    #     self.goto(random.randint(-250,250), 400)
    #     self.cars = self.segments.append(number_of_cars)
    
    def create_car(self):
        # Create a random car with a 1 in 6 chance.
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(COLORS[random.randint(0,5)])
            new_car.goto(300,random.randint(-200,200))
            self.all_cars.append(new_car)
        
