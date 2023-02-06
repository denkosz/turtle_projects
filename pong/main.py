from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_pong = Paddle((350, 0))
l_pong = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_pong.up, "Up")
screen.onkey(r_pong.down, "Down")

screen.onkey(l_pong.up, "w")
screen.onkey(l_pong.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    if ball.distance(r_pong) < 50 and ball.xcor() > 320 or ball.distance(l_pong) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.resetposition()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.resetposition()
        scoreboard.r_point()

screen.exitonclick()
