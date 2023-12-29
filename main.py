from turtle import Screen
from paddle import Paddle
import time

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
X_POSITION = (SCREEN_WIDTH / 2) - 40
STARTING_POSITION_1 = (-X_POSITION, 0)
STARTING_POSITION_2 = (X_POSITION-10, 0)

# Screen Setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Veregorns Pong Game')
screen.tracer(0) # Turn turtle animation off so we can decide when to update the screen

# Variable Setup
paddle1 = Paddle(STARTING_POSITION_1)
paddle2 = Paddle(STARTING_POSITION_2)

# Event Listeners
screen.listen()
screen.onkey(paddle1.move_up, "w")
screen.onkey(paddle1.move_down, "s")
screen.onkey(paddle2.move_up, "Up")
screen.onkey(paddle2.move_down, "Down")

# Game main loop
game_is_on = True

while game_is_on:
    screen.update() # So all the segments of paddles move together
    time.sleep(0.03) # So I can see how paddles and ball move as slow as I want





# Windows closes on click
screen.exitonclick()