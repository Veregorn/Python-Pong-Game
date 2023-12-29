from turtle import Turtle

# Constants
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self, starting_position) -> None:
        self.body = Turtle(shape="square")
        self.body.color("white")
        self.body.shapesize(stretch_wid=5, stretch_len=1)
        self.body.penup()
        self.body.goto(starting_position)

    def move_up(self):
        self.body.sety(self.body.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.body.sety(self.body.ycor() - MOVE_DISTANCE)