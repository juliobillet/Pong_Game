from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_paddle_score = 0
        self.l_paddle_score = 0

    def l_score(self):
        self.l_paddle_score += 1

    def r_score(self):
        self.r_paddle_score += 1

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.l_paddle_score}", align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(arg=f"{self.r_paddle_score}", align="center", font=("Courier", 70, "normal"))
