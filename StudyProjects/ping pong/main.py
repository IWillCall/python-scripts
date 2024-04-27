from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PyPong')
screen.tracer(0)

COORDS1 = (350, 0)
COORDS2 = (-350, 0)

r_paddle = Paddle(COORDS1)
l_paddle = Paddle(COORDS2)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()

screen.onkeypress(key='Up', fun=r_paddle.move_up)
screen.onkeypress(key='Down', fun=r_paddle.move_down)

screen.onkeypress(key='w', fun=l_paddle.move_up)
screen.onkeypress(key='s', fun=l_paddle.move_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        
    # detect r_paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()
        
    # detect l_paddle misses
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()