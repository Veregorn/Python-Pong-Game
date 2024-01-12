from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
X_POSITION = (SCREEN_WIDTH / 2) - 10
STARTING_POSITION_1 = (-X_POSITION, 0)
STARTING_POSITION_2 = (X_POSITION-10, 0)
BALL_STARTING_POSITION = (0, 0)

# Screen Setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Veregorns Pong Game')
screen.tracer(0) # Turn turtle animation off so we can decide when to update the screen

# Variable Setup
paddle_left = Paddle(STARTING_POSITION_1, (SCREEN_HEIGHT / 2) - 55)
paddle_right = Paddle(STARTING_POSITION_2, (SCREEN_HEIGHT / 2) - 55)
ball = Ball(BALL_STARTING_POSITION, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

pl_up_pressed = False
pl_down_pressed = False
pr_up_pressed = False
pr_down_pressed = False

# Functions that change key pressed variable states
def pl_up_press():
    global pl_up_pressed
    pl_up_pressed = True

def pl_down_press():
    global pl_down_pressed
    pl_down_pressed = True

def pr_up_press():
    global pr_up_pressed
    pr_up_pressed = True

def pr_down_press():
    global pr_down_pressed
    pr_down_pressed = True

def pl_up_release():
    global pl_up_pressed
    pl_up_pressed = False

def pl_down_release():
    global pl_down_pressed
    pl_down_pressed = False

def pr_up_release():
    global pr_up_pressed
    pr_up_pressed = False

def pr_down_release():
    global pr_down_pressed
    pr_down_pressed = False

# Event Listeners
screen.listen()
screen.onkeypress(pl_up_press, "w")
screen.onkeypress(pl_down_press, "s")
screen.onkeypress(pr_up_press, "Up")
screen.onkeypress(pr_down_press, "Down")
screen.onkeyrelease(pl_up_release, "w")
screen.onkeyrelease(pl_down_release, "s")
screen.onkeyrelease(pr_up_release, "Up")
screen.onkeyrelease(pr_down_release, "Down")

# Game main loop
game_is_on = True

while game_is_on:
    screen.update() # So all the segments of paddles move together
    time.sleep(0.03) # So I can see how paddles and ball move as slow as I want

    if pl_up_pressed:
        paddle_left.move_up()

    if pl_down_pressed:
        paddle_left.move_down()

    if pr_up_pressed:
        paddle_right.move_up()

    if pr_down_pressed:
        paddle_right.move_down()

    ball.move()

    # Detect collisions with paddles
    if (ball.distance(paddle_right) < 50 and ball.get_xcor() > X_POSITION - 30) or (ball.distance(paddle_left) < 50 and ball.get_xcor() < -X_POSITION + 20):
        ball.rebound()

    # Detect when a point is win
    if ball.get_xcor() > X_POSITION or ball.get_xcor() < -X_POSITION:
        ball.goto(BALL_STARTING_POSITION)
        ball.change_dir()



# Windows closes on click
screen.exitonclick()