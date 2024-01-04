from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
X_POSITION = (SCREEN_WIDTH / 2) - 40
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
paddle1 = Paddle(STARTING_POSITION_1)
paddle2 = Paddle(STARTING_POSITION_2)
ball = Ball(BALL_STARTING_POSITION)

p1_up_pressed = False
p1_down_pressed = False
p2_up_pressed = False
p2_down_pressed = False

# Functions that change key pressed variable states
def p1_up_press():
    global p1_up_pressed
    p1_up_pressed = True

def p1_down_press():
    global p1_down_pressed
    p1_down_pressed = True

def p2_up_press():
    global p2_up_pressed
    p2_up_pressed = True

def p2_down_press():
    global p2_down_pressed
    p2_down_pressed = True

def p1_up_release():
    global p1_up_pressed
    p1_up_pressed = False

def p1_down_release():
    global p1_down_pressed
    p1_down_pressed = False

def p2_up_release():
    global p2_up_pressed
    p2_up_pressed = False

def p2_down_release():
    global p2_down_pressed
    p2_down_pressed = False

# Event Listeners
screen.listen()
screen.onkeypress(p1_up_press, "w")
screen.onkeypress(p1_down_press, "s")
screen.onkeypress(p2_up_press, "Up")
screen.onkeypress(p2_down_press, "Down")
screen.onkeyrelease(p1_up_release, "w")
screen.onkeyrelease(p1_down_release, "s")
screen.onkeyrelease(p2_up_release, "Up")
screen.onkeyrelease(p2_down_release, "Down")

# Game main loop
game_is_on = True

while game_is_on:
    screen.update() # So all the segments of paddles move together
    time.sleep(0.03) # So I can see how paddles and ball move as slow as I want

    if p1_up_pressed:
        paddle1.move_up()

    if p1_down_pressed:
        paddle1.move_down()

    if p2_up_pressed:
        paddle2.move_up()

    if p2_down_pressed:
        paddle2.move_down()

    ball.move()



# Windows closes on click
screen.exitonclick()