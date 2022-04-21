from turtle import Turtle

ALIGN = "center"
FONT = ("arial", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.pencolor("white")
        self.speed("fastest")
        self.pu()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def add_score(self):
        self.score = self.score + 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as data:
                data.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)


