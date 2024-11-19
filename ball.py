from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.y_pos = y_pos
        # self.x_pos = x_pos
        self.color('white')
        self.shape('circle')
        self.shapesize(1, 1)
        self.x_move = 0.1
        self.y_move = 0.1
        # self.goto(0, 0)
        # self.penup()
        # self.goto(self.x_pos, self.y_pos)

    # def go_corner(self, x_pos, y_pos):
    #     self.penup()
    #     self.speed('slowest')
    #     self.goto(x_pos, y_pos)

    # def go_corner(self, dist):
    #     self.penup()
    #     self.speed('slowest')
    #     self.forward(dist)

    def move(self):
        self.penup()
        self.speed('slowest')
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x, new_y)

    # def move_left(self):
    #     self.penup()
    #     self.speed('slowest')
    #     new_x = self.xcor()-self.x_move
    #     new_y = self.ycor()+ self.y_move
    #     self.goto(new_x, new_y)

    # def after_bounce(self):
    #     self.penup()
    #     self.speed('slowest')
    #     new_x = self.xcor() + 0.2
    #     new_y = self.ycor() - 0.3
    #     self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1


    def bounce_x(self):
        self.x_move *= -1

    def increase_speed(self):
        self.x_move *= 3.1
        self.y_move *= 3.1

    def reset_position(self):
        # self.penup()
        self.speed('slowest')
        self.goto(0, 0)
        self.x_move = 0.1
        self.y_move = 0.1






