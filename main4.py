from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_back():
    tim.back(10)


def right_clock():
    tim.right(10)


def left_clock():
    tim.left(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(right_clock, "d")
screen.onkey(left_clock, "a")
screen.onkey(clear, "c")
screen.exitonclick()
