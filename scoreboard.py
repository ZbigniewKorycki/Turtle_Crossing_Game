from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-230, y=260)
        self.pencolor("white")
        self.show_level()

    def show_level(self):
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def update_level(self):
        self.clear()
        self.level += 1
        self.show_level()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
