from turtle import Screen
import time

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Veregorns Pong Game')
screen.tracer(0) # Turn turtle animation off so we can decide when to update the screen




# Game main loop
game_is_on = True

while game_is_on:
    screen.update() # So all the segments of paddles move together
    time.sleep(0.1) # So I can see how paddles and ball move as slow as I want





# Windows closes on click
screen.exitonclick()