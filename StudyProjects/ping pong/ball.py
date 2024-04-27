from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.move_distance = {'x':10, 'y':10}
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.move_distance['x']
        new_y = self.ycor() + self.move_distance['y']
        
        self.goto(x = new_x, y = new_y)
        
    def bounce_y(self):
        self.move_distance['y'] *= -1
        
    def bounce_x(self):
        self.move_distance['x'] *= -1
        self.move_speed *= 0.9
        
    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
