from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(arg=f"Player A:{self.right_score}", align="center", font=("courier", 20, "normal"))
        self.goto(100, 220)
        self.write(arg=f"Player B:{self.left_score}", align="center", font=("courier", 20, "normal"))

    def r_score(self):
        self.right_score += 1

    def l_score(self):
        self.left_score += 1

    def winner(self):

        if self.left_score == 3:

            self.goto(0, 0)
            self.write("Winner is Player B", align="center", font=("courier", 30, "normal"))
            return False

        if self.right_score == 3:
            self.goto(0, 0)
            self.write("Winner is Player A", align="center", font=("courier", 30, "normal"))
            return False

        return True



