import turtle
from turtle import Turtle, Screen
import random
timmy = Turtle()
turtle.colormode(255)
timmy.shape("arrow")
timmy.pensize(10)
timmy.speed(8)
direction = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for y in range(200):
    timmy.color(random_color())
    timmy.setheading(random.choice(direction))
    timmy.forward(30)

screen = Screen()
screen.exitonclick()
