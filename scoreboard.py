from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.write(arg=f"scoreboard: {0}", align="center", font=("Arial", 8, "normal"))

