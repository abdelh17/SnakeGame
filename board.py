from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGN = "center"


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!!!", align="center", font=("Courier", 50, "normal"))
