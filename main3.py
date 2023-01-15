#import colorgram
import random
from turtle import Turtle, Screen
import turtle
turtle.colormode(255)
screen = Screen()
timmy = Turtle()
timmy.speed(20)
timmy.hideturtle()
color_list = [(233, 233, 232), (231, 233, 237), (235, 231, 233), (224, 233, 227), (207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 26, 49), (222, 206, 108), (132, 177, 203),
              (45, 55, 104), (158, 46, 83), (169, 160, 39), (129, 189, 143), (83, 20, 44), (38, 43, 67), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31),
              (88, 157, 92), (78, 153, 165), (195, 79, 72), (161, 201, 219), (45, 74, 77), (79, 74, 44), (57, 125, 121), (218, 176, 188), (167, 206, 168), (220, 182, 168)]

def draw_circle():
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.down()

def move_up():
    y = -200
    for _ in range(10):
        timmy.penup()
        timmy.setpos(-200, y)
        timmy.down()
        draw_circle()
        y += 50

move_up()

screen.exitonclick()
# colors = colorgram.extract('spot1.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#print(rgb_colors)


