from turtle import Turtle

ALIGN = "center"
FONT = ("arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.speed("fastest")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def refresh(self):
        self.clear()
        self.score = self.score + 1
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)


