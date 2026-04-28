# import turtle

# pen = turtle.Turtle()

# for i in range(5):
#     pen.forward(150)
#     pen.right(144)

# turtle.done()

# import turtle
# pen = turtle.Turtle()

# pen.circle(100)
# turtle.done()

import turtle
my_wn = turtle.Screen()
my_wn.bgcolor("light blue")
my_wn.title("Turtle")
pen = turtle.Turtle()
size = 0
while True : 
    for i in range(4):
        pen.forward(size + 1)
        pen.right(90)
        size = size - 5
    size = size + 1
turtle.done()