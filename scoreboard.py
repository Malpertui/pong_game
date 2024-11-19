from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score_a = 0
        self.score_b = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_b, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.score_a, align='center', font=('Courier', 80, 'normal'))

    def score_b_update(self):
        self.score_b += 1
        self.clear()
        self.update_scoreboard()

    def score_a_update(self):
        self.score_a += 1
        self.clear()
        self.update_scoreboard()