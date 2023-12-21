from turtle import Turtle

# Constants
MOVE_DISTANCE = 20

class Paddle:

    def __init__(self, starting_positions) -> None:
        self.segments = []
        self.create_paddle(starting_positions)
        self.head = self.segments[0]

    def create_paddle(self, starting_positions):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move(self):
        pass