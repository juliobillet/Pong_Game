from turtle import Turtle

Y_LIMIT = 240


class Paddle(Turtle):

    def __init__(self, paddle_pos):
        super(Paddle, self).__init__()
        self.paddle_position = paddle_pos
        self.paddle = self.create_paddle()

    def create_paddle(self):
        paddle_obj = Turtle(shape="square")
        paddle_obj.penup()
        paddle_obj.color("white")
        paddle_obj.goto(self.paddle_position)
        paddle_obj.resizemode("user")
        paddle_obj.shapesize(stretch_wid=5, stretch_len=1)
        return paddle_obj

    def go_up(self):
        if self.paddle.ycor() < Y_LIMIT:
            new_y = self.paddle.ycor() + 20
            self.paddle.goto(x=self.paddle.xcor(), y=new_y)

    def go_down(self):
        if self.paddle.ycor() > -Y_LIMIT:
            new_y = self.paddle.ycor() - 20
            self.paddle.goto(x=self.paddle.xcor(), y=new_y)
