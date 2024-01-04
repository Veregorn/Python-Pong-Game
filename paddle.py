from turtle import Turtle

# Constants
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, starting_position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)