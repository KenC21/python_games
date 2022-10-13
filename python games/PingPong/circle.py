from turtle import Turtle
from random import randint


class Circle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = .05

    def move_circle(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)

    def bounce_ball_y(self):
        self.y_move *= -1

    def bounce_ball_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def circle_reset(self):
        self.goto(0, 0)
        self.move_speed = .05
        self.x_move *= -1
