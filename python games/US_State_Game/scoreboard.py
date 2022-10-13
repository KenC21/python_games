from turtle import Turtle

FONT = ("courier", 12, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()

    def move_answer(self, xcoor, ycoor, answer):
        self.goto(xcoor, ycoor)
        self.write(answer, align="center", font=FONT)
