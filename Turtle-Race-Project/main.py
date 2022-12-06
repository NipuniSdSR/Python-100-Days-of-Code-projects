# Turtle Race project
from turtle import Turtle, Screen
import random

screen = Screen()

race_started = False

# todo: screen cutermize
screen.setup(width=500, height=400)
# pop-up screen
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make your bet", prompt=f"Whic turtle will win the race? Enter a color:\n {colors[:] }")


racers = []

for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=100 + index * (-40))
    racers.append(new_turtle)


if user_bet:
    race_started = True

while race_started:

    for turtle in racers:
        # selecting the winning turtle
        if turtle.xcor() > 230:
            race_started = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The {winner_color} turtle is the  winner")
            else:
                print(f"You've lost! The {winner_color} turtle is the  winner")


        # assign random speed for each turtle
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()