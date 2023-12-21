from turtle import Turtle

# Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle:

    def __init__(self, starting_positions) -> None:
        self.segments = []
        self.create_paddle(starting_positions)
        self.head = self.segments[0]
        self.head.setheading(UP)
        self.tail = self.segments[len(self.segments - 1)]
        self.tail.setheading(DOWN)

    def create_paddle(self, starting_positions):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def move_up(self):
        for seg_num in range(len(self.segments - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def move_down(self):
        for seg_num in range(0, len(self.segments - 1), 1):
            new_x = self.segments[seg_num + 1].xcor()
            new_y = self.segments[seg_num + 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.tail.forward(MOVE_DISTANCE)