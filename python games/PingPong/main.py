from turtle import Screen
from paddle import Paddle
from circle import Circle
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

circle = Circle()
scoreboard = ScoreBoard()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(key="Up", fun=r_paddle.move_up_right)
screen.onkey(key="Down", fun=r_paddle.move_down_right)
screen.onkey(key="w", fun=l_paddle.move_up_left)
screen.onkey(key="s", fun=l_paddle.move_down_left)


def game_new():
    game = True

    circle.circle_reset()
    l_paddle.paddle_start()
    r_paddle.paddle_start()

    while game:
        time.sleep(circle.move_speed)
        circle.move_circle()
        scoreboard.update_scoreboard()

        # Detect collision with wall
        if circle.ycor() > 280 or circle.ycor() < -280:
            circle.bounce_ball_y()

        # Detect collision with paddle
        if circle.distance(r_paddle) < 60 and circle.xcor() > 330 or circle.distance(
                l_paddle) < 60 and circle.xcor() < -330:
            circle.bounce_ball_x()

        if circle.xcor() > 380:
            scoreboard.r_score()
            game = False

        if circle.xcor() < -380:
            scoreboard.l_score()
            game = False

        screen.update()


game_continue = True

while game_continue:

    game_new()
    check = scoreboard.winner()

    if not check:
        scoreboard.update_scoreboard()
        scoreboard.winner()
        game_continue = False

screen.exitonclick()
