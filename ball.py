from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.TOP_LIMIT = 285
        self.BOTTOM_LIMIT = -290
        self.x_constant = 10
        self.y_constant = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

    def is_collided_with_wall(self):
        return abs(self.ycor() - self.TOP_LIMIT) <= 10 or abs(self.ycor() - self.BOTTOM_LIMIT) <= 10

    def move(self):
        self.collision_with_walls()
        new_x = self.xcor() + self.x_constant
        new_y = self.ycor() + self.y_constant
        self.goto(new_x, new_y)

    def collision_with_walls(self):
        if self.is_collided_with_wall():
            self.y_constant *= -1

    def change_x_constant(self):
        self.x_constant *= -1
