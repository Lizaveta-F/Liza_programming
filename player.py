from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def up_move(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.setposition(STARTING_POSITION)

    def is_at_the_end(self):
        if self.ycor() > 280:
            return True
        else:
            return False


