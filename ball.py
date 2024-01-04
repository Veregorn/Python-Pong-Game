from turtle import Turtle

# Constants
MOVE_DISTANCE = 20

class Ball(Turtle):

    def __init__(self, starting_position) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(starting_position)

    def move(self):
        self.goto(self.xcor() + 10, self.ycor() + 10)