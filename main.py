import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)


tim = Turtle()
tim.shape("turtle")
tim.color("red")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#This is my method on how to draw a dashed line
# for _ in range(50):
#     tim.forward(10)
#     tim.color("white")
#     tim.forward(10)
#     tim.color("black")
#

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3,11):
#     draw_shape(shape_side_n)
#     tim.color(random.choice(color))


# color = ["medium blue","deep pink","indigo","dim gray","lime","crimson","pale violet red","thistle"]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

# directions = [0,90,180,270]
# tim.pensize(5)
tim.speed("fastest")


# for _ in range(500):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random_color())


def draw_spi(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)

draw_spi(5)


screen = Screen()
screen.exitonclick()