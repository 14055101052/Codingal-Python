# import turtle

# pen = turtle.Turtle()
# pen.speed(2)
# pen.color("Red")
# pen.fillcolor("Cyan")

# pen.begin_fill()

# for i in range(4):
#     pen.forward(100)
#     pen.right(90)

# pen.end_fill()
# turtle.done()

import turtle
pen = turtle.Turtle()

number_sides = 6
side_length = 80

for i in range(number_sides):
    pen.forward(side_length)
    pen.right(360/number_sides)
turtle.done()

