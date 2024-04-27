from turtle import Turtle

STARTING_POSITIONS = [(40, 0), (20, 0), (0, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_body_part(position)

    def add_body_part(self, position):
        new_part = Turtle("square")
        new_part.penup()
        new_part.color("white")
        new_part.goto(position)
        self.snake_body.append(new_part)

    def reset(self):
        for snake_part in self.snake_body:
            snake_part.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_body_part(self.snake_body[-1].position())

    def move(self):
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_num - 1].xcor()
            new_y = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto((new_x, new_y))
        self.snake_body[0].forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() != RIGHT:
            self.head.seth(RIGHT)

    def move_left(self):
        if self.head.heading() != LEFT:
            self.head.seth(LEFT)

    def move_up(self):
        if self.head.heading() != UP:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != DOWN:
            self.head.seth(DOWN)
