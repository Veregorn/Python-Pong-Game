from turtle import Turtle

# Constants
MOVE_DISTANCE = 20
REBOUND_ANGLE = 10

class Ball(Turtle):

    def __init__(self, starting_position, x_limit, y_limit) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(starting_position)
        self.going_top = True
        self.going_right = True 

    def get_xcor(self):
        return self.xcor()
    
    def get_ycor(self):
        return self.ycor()
    
    def move(self):
        if self.going_top:
            if self.going_right:
                if self.ycor() < self.y_limit - 10:
                    self.goto(self.xcor() + 10, self.ycor() + REBOUND_ANGLE)
                else:
                    self.going_top = False
                    self.goto(self.xcor() + 10, self.ycor() - REBOUND_ANGLE)
            else:
                if self.ycor() < self.y_limit - 10:
                    self.goto(self.xcor() - 10, self.ycor() + REBOUND_ANGLE)
                else:
                    self.going_top = False
                    self.goto(self.xcor() - 10, self.ycor() - REBOUND_ANGLE)
        else:
            if self.going_right:
                if self.ycor() > -self.y_limit + 10:
                    self.goto(self.xcor() + 10, self.ycor() - REBOUND_ANGLE)
                else:
                    self.going_top = True
                    self.goto(self.xcor() + 10, self.ycor() + REBOUND_ANGLE)
            else:
                if self.ycor() > -self.y_limit + 10:
                    self.goto(self.xcor() - 10, self.ycor() - REBOUND_ANGLE)
                else:
                    self.going_top = True
                    self.goto(self.xcor() - 10, self.ycor() + REBOUND_ANGLE)

    def rebound(self):
        if self.going_top:
            if self.going_right:
                self.goto(self.xcor() - 10, self.ycor() + REBOUND_ANGLE)
                self.going_right = False
            else:
                self.goto(self.xcor() + 10, self.ycor() + REBOUND_ANGLE)
                self.going_right = True
        else:
            if self.going_right:
                self.goto(self.xcor() - 10, self.ycor() - REBOUND_ANGLE)
                self.going_right = False
            else:
                self.goto(self.xcor() + 10, self.ycor() - REBOUND_ANGLE)
                self.going_right = True