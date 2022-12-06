import turtle
from city import City

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Access specific coordinate in the screen:Google search
# To place each

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop() # keep the screen open


screen.tracer(0)

# getting csv data

import pandas

data = pandas.read_csv("50_states.csv")
states = data["state"]

# check if the guess is among the 50 states

# print(states.isin([answer_state]))
game_is_on = True
record = []

while game_is_on:
    # pop-up dialog box
    answer_state = screen.textinput(title=f"{len(record)}/50 Guess the state", prompt="What's the state name? ")
    answer_state = answer_state.title()

    screen.update()

    if answer_state in states.values:
        record.append(answer_state)
        state_row = data[data["state"] == answer_state]  # dataframe
        city = City(state_row=state_row)
        city.details()


screen.exitonclick()
