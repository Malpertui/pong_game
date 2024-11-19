from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.teleport(self.x_pos, self.y_pos)

    def go_up(self):
        self.penup()
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        self.penup()
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)











