from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.computer_score = 0
        self.user_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.computer_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.user_score, align="center", font=("Courier", 80, "normal"))

    def computer_point(self):
        self.computer_score += 1
        self.update_scoreboard()

    def user_point(self):
        self.user_score += 1
        self.update_scoreboard()
