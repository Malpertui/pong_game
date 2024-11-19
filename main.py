from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("-=Pong Game=-")

paddle_a = Turtle()
paddle_a.color('white')
paddle_a.shape('square')
X_POS = 350
Y_POS = 0
paddle_a.teleport(X_POS, Y_POS)
# paddle_a.resizemode('user')
paddle_a.shapesize(5, 1)
# paddle_a.turtlesize(20, 20)

def up():
    # paddle_a.setheading(90)
    paddle_a.penup()
    # x = X_POS
    # y = Y_POS
    global Y_POS
    global X_POS
    Y_POS += 20
    paddle_a.goto(X_POS, Y_POS)




def down():
    # paddle_a.setheading(270)
    paddle_a.penup()
    # paddle_a.forward(20)
    global Y_POS
    global X_POS
    Y_POS -= 20
    paddle_a.goto(X_POS, Y_POS)


screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")

screen.exitonclick()