from turtle import Screen

from paddle import Paddle

from ball import Ball
from scoreboard import Scoreboard

# import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("-=Pong Game=-")
screen.tracer(0)

paddle_a = Paddle(350, 0)
paddle_b = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

# ball.go_corner(380, 285)
# ball.go_corner(100)


screen.listen()
screen.onkeypress(paddle_a.go_up, "Up")
screen.onkeypress(paddle_a.go_down, "Down")

# screen.onkey(paddle_a.go_up, "Up")
# screen.onkey(paddle_a.go_down, "Down")



screen.onkeypress(paddle_b.go_up, "w")
screen.onkeypress(paddle_b.go_down, "s")

# screen.onkey(paddle_b.go_up, "w")
# screen.onkey(paddle_b.go_down, "s")

game_is_on = True

while game_is_on:

    screen.update()
    ball.move()

    if ball.ycor() > 295 or ball.ycor() < -295:
        ball.bounce_y()


    # Detect collision with r_paddle
    if ball.xcor() > 390:
        ball.reset()
        # ball.clear()
        ball = Ball()
        ball.bounce_x()
        scoreboard.score_b_update()

    elif ball.xcor() < -390:
        ball.reset()
        ball = Ball()
        ball.move()
        scoreboard.score_a_update()
        # ball.bounce_x()

    elif ball.distance(paddle_a) < 50 and ball.xcor() > 330 \
        or ball.distance(paddle_b) < 50 and  ball.xcor() < -330:
        print('Made contact')
        ball.bounce_x()
        ball.increase_speed()



screen.exitonclick()