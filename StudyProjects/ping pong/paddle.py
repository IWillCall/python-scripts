from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.color('white')
        self.penup()
        self.teleport(x = coords[0], y = coords[1])
        self.seth(90)
        self.score = 0
    
    def move_up(self):
        if self.ycor() < 250:
            self.forward(MOVE_DISTANCE)
        
    def move_down(self):
        if self.ycor() > -250:
            self.backward(MOVE_DISTANCE)
            
    def increase_score(self):
        self.score += 1