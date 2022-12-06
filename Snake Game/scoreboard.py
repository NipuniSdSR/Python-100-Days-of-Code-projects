from turtle import Turtle

ALIGNMENT = "center"
FONT = ('courier', 16, 'normal')




class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("../data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score : {self.score}   high score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def set_high_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("../data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
