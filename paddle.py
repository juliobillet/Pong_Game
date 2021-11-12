from turtle import Turtle

Y_LIMIT = 240


class Paddle(Turtle):

    def __init__(self, paddle_pos):
        super(Paddle, self).__init__()
        self.paddle_position = paddle_pos
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(self.paddle_position)
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.draw_line_at_center()

    def go_up(self):
        if self.ycor() < Y_LIMIT:
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        if self.ycor() > -Y_LIMIT:
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)

    @staticmethod
    def draw_line_at_center():
        draw_line = Turtle()
        draw_line.pencolor("white")
        draw_line.hideturtle()
        draw_line.penup()
        draw_line.setpos(0, -340)
        draw_line.pensize(10)
        draw_line.setheading(90)
        for i in range(10):
            draw_line.forward(40)
            draw_line.pendown()
            draw_line.forward(40)
            draw_line.penup()
