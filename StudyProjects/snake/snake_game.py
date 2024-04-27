from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

MAP_EDGE = 290

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("PySnake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    # collision with wall
    if (
        snake.head.xcor() > MAP_EDGE
        or snake.head.xcor() < -1 * MAP_EDGE
        or snake.head.ycor() > MAP_EDGE
        or snake.head.ycor() < -1 * MAP_EDGE
    ):
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for snake_part in snake.snake_body[1:]:
        if snake.head.distance(snake_part) < 10:
            pass
        elif snake.head.distance(snake_part) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
