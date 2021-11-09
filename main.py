from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

R_PADDLE_POSITION = (350, 0)
L_PADDLE_POSITION = (-360, 0)

game_is_on = True
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(paddle_pos=R_PADDLE_POSITION)
l_paddle = Paddle(paddle_pos=L_PADDLE_POSITION)
ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

while game_is_on:
    screen.update()
    print(f"R_Paddle: {r_paddle.pos()}")
    ball.move()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        print("made contact")
    time.sleep(0.1)

screen.exitonclick()
