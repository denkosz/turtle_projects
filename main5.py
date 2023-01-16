from turtle import Turtle, Screen
import random

race_end = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
m = [150, 100, 50, -50, -100, -150]
all_turtles = []

for turtle_num in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_num])
    new_turtle.penup()
    new_turtle.goto(-230, m[turtle_num])
    all_turtles.append(new_turtle)

if user_bet:
    race_end = True
while race_end:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_end = False
            #winning turtle color
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
