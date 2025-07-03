import colorgram
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
color_list = [(203, 172, 108),  (153, 180, 195), (152, 186, 174), (193, 161, 176), (214, 203, 113),  (174, 188, 213), (161, 213, 187), (161, 203, 215), (114, 123, 186), (177, 160, 71), (213, 182, 181), (198, 207, 46), (105, 114, 142), (164, 121, 51)]
tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1 , number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
