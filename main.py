from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Constant variables, never to be changed.
R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-360, 0)

# Global Variables
game_is_on = True

# Create screen and its settings.
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create all the objects in the game.
scoreboard = Scoreboard()
r_paddle = Paddle(paddle_pos=R_PADDLE_POSITION)
l_paddle = Paddle(paddle_pos=L_PADDLE_POSITION)
ball = Ball()

# Detect Keys pressed to move the paddles.
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Game loop.
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with paddles and increases the ball speed each time it hits a paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > R_PADDLE_POSITION[0] - 30 or ball.distance(l_paddle) < 50 and \
            ball.xcor() < L_PADDLE_POSITION[0] + 30:
        ball.change_x_constant()
        if ball.move_speed > 0.01:
            ball.move_speed -= 0.01

    # Detect when R paddle misses the ball.
    if ball.xcor() > R_PADDLE_POSITION[0] + 30:
        ball.reset_ball_position()
        scoreboard.l_score()

    # Detect when L paddle misses the ball.
    if ball.xcor() < L_PADDLE_POSITION[0] - 30:
        ball.reset_ball_position()
        scoreboard.r_score()
    # Update the score each loop.
    scoreboard.update_score()
    # The speed of the ball but also the speed of the entire loop and response of the game.
    time.sleep(ball.move_speed)

# Exit on click function for the screen, just because. xD
screen.exitonclick()
