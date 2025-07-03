import turtle
from turtle import Turtle , Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet",prompt="Witch Turtle will win the race? Enter a Rainbow color: ")
colors = ["red","orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []
print(user_bet)

for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:


    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won , The winning color is {winning_color}!")
            else:
                print(f"You have lost , The winning color is {winning_color}!")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-220, y =-100 )
# tim.color("red")
#
# jack = Turtle(shape="turtle")
# jack.penup()
# jack.goto(x=-220, y=-50)
# jack.color("orange")
#
# dom = Turtle(shape="turtle")
# dom.penup()
# dom.goto(x=-220, y=0)
# dom.color("yellow")
#
# tom = Turtle(shape="turtle")
# tom.penup()
# tom.goto(x=-220, y=+50)
# tom.color("green")
#
# kat = Turtle(shape="turtle")
# kat.penup()
# kat.goto(x=-220, y=+100)
# kat.color("blue")
#
# matt = Turtle(shape="turtle")
# matt.penup()
# matt.goto(x=-220, y=+150)
# matt.color("purple")






screen.exitonclick()
