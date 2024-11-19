from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("-=Pong Game=-")

paddle_c = Turtle()
paddle_c.color('white')
paddle_c.shape('square')
X_POS = 350
Y_POS = 0
paddle_c.teleport(X_POS, Y_POS)
paddle_c.shapesize(5, 1)

def up():
    paddle_c.penup()
    global Y_POS
    global X_POS
    Y_POS += 20
    paddle_c.goto(X_POS, Y_POS)

def down():
    paddle_c.penup()
    global Y_POS
    global X_POS
    Y_POS -= 20
    paddle_c.goto(X_POS, Y_POS)

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")

screen.exitonclick()