from turtle import Turtle


class City(Turtle):
    def __init__(self, state_row):
        super().__init__()
        self.x = int(state_row.x)
        self.y = int(state_row.y)
        self.state = state_row.state
        self.penup()
        self.hideturtle()
        self.goto(x=self.x, y=self.y)
        self.write(f"{self.state}")

    def details(self):
        print(f"state: {self.state}, x= {self.x}, y= {self.y}")
