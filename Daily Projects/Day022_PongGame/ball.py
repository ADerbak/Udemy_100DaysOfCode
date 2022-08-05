from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        # Ball creation
        self.penup()
        self.shape('circle')
        self.color('white')
        self.y_direction = 1
        self.x_direction = 1
        self.move_speed = 0.05
        
    def move(self):
        
        # Make the ball continue upward or downward until it reaches an edge
        if self.ycor() == 300:
            self.y_direction = -1
        elif self.ycor() == -300:
            self.y_direction = 1
            
                    
        new_y = self.ycor() + (10 * self.y_direction)            
        new_x = self.xcor() + (5 * self.x_direction)
        self.goto(new_x, new_y)
        
    def reset_position(self):
        self.goto(0,0)
        self.x_direction *= -1
        self.move_speed = 0.05
        