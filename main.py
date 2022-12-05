from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "purple"]
y_positions = [-100, -50, 0, 50, 100]
all_turtle = []

for index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput(title="The is ended", prompt=f"You have won. The {winning_color} turtle is a winner!")
            else:
                screen.textinput(title="The is ended",
                                 prompt=f"You lost. The {winning_color} turtle is a winner!")
            print(turtle.pencolor)
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)

screen.exitonclick()
