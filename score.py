from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",25,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("Maroon")

        self.penup()
        self.goto(0,265)
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.write(f"game over",align = ALIGNMENT,font =FONT)