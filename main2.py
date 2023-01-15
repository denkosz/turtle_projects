from turtle import Turtle, Screen
import random
import turtle
timmy = Turtle()
timmy.shape("arrow")
turtle.colormode(255)
timmy.speed(30)
color_loop = ["Blue", "Green", "Red", "Black", "Pink", "Yellow", "Grey"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw(size_gap):
    for i in range(int(360 / size_gap)):
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_gap)
        timmy.color(random_color())

draw(5)

screen = Screen()
screen.exitonclick()
