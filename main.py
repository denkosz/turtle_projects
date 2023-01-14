from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

range_pic = [3, 4, 5, 6, 7, 8, 9]
color_loop = ["Blue", "Green", "Red", "Black", "Pink", "Yellow", "Grey"]
right_loop = [120, 90, 72, 60, 51.4, 45, 40]

for i in range(len(range_pic)):
    timmy.color(color_loop[i])
    loop = range_pic[i]
    for y in range(loop):
        timmy.right(right_loop[i])
        timmy.forward(100)


screen = Screen()
screen.exitonclick()

