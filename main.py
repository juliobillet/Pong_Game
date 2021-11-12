from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-360, 0)

game_is_on = True
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
r_paddle = Paddle(paddle_pos=R_PADDLE_POSITION)
l_paddle = Paddle(paddle_pos=L_PADDLE_POSITION)
ball = Ball()

# Detect Keys pressed to move the paddles
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    ball.move()
    print(ball.move_speed)

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > R_PADDLE_POSITION[0] - 30 or ball.distance(l_paddle) < 50 and \
            ball.xcor() < L_PADDLE_POSITION[0] + 30:
        ball.change_x_constant()
        if ball.move_speed > 0.01:
            ball.move_speed -= 0.01

    # Detect when R paddle misses the ball
    if ball.xcor() > R_PADDLE_POSITION[0] + 30:
        ball.reset_ball_position()
        scoreboard.l_score()

    # Detect when L paddle misses the ball
    if ball.xcor() < L_PADDLE_POSITION[0] - 30:
        ball.reset_ball_position()
        scoreboard.r_score()

    scoreboard.update_score()
    time.sleep(ball.move_speed)

screen.exitonclick()
