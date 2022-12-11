from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
# screen.tracer(0)

segments = []

for index in range(-40,1,20):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.pensize(10)
    turtle.setposition(x=index, y=0)
    segments.append(turtle)

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)



screen.exitonclick()
