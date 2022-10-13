from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        self.start_xcor = self.xcor()
        self.start_ycor = self.ycor()


    def move_up_left(self):
        current_ycor = self.ycor() + 40
        self.goto(x=self.xcor(), y=current_ycor)

    def move_down_left(self):
        current_ycor = self.ycor() - 40
        self.goto(x=self.xcor(), y=current_ycor)

    def move_up_right(self):
        current_ycor = self.ycor() + 40
        self.goto(x=self.xcor(), y=current_ycor)

    def move_down_right(self):
        current_ycor = self.ycor() - 40
        self.goto(x=self.xcor(), y=current_ycor)

    def paddle_start(self):
        self.goto(self.start_xcor, self.start_ycor)
