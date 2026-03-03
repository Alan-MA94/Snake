from turtle import Turtle

FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()

    def scoreboard(self):
        self.clear()
        self.goto(-30, 350)
        self.write(f"Score: {self.score}        Highscore:{self.highscore}", font= FONT)

    def increase_score(self):
        self.score += 1
        self.scoreboard()


    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
        self.score = 0
        self.scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"    Game Over\nYour Score is: {self.score}", align= "center", font= FONT)

