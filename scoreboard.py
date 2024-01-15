from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, y_limit) -> None:
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.y_limit = y_limit
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(-100, self.y_limit - 100)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, self.y_limit - 100)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def give_point(self, who):
        if who == 'left':
            self.l_score += 1
        elif who == 'right':
            self.r_score += 1
        
        self.clear()
        self.update_scoreboard()