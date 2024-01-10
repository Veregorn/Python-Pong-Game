from turtle import Turtle

# Constants
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, starting_position, y_limit) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_position)
        self.y_limit = y_limit

    def move_up(self):
        if self.ycor() < self.y_limit:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -self.y_limit:
            self.sety(self.ycor() - MOVE_DISTANCE)