from turtle import Turtle

FONT = ("Arial", 14, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 265)
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align = "left", font = FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write(f"Game is Over: {self.level}", align = "center", font = FONT)