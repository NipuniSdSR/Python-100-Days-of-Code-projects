# Angela 's code
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
# print(states)
guessed_states = []
while len(guessed_states) < 50:
    # pop-up dialog box
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50  Guess the state", prompt="What's the state name? ")
    answer_state = answer_state.title()

# If answer_state is one of the states in all the states of the 50_states.csv
    # f they got it right:
        #create a turtle to write the name of the state at the state's x and y coordinate
    if answer_state == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data_frame = pandas.DataFrame(missing_states)
        new_data_frame.to_csv("states_to_learn.csv")
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = data[data.state == answer_state]
        t.goto(x=int(state.x), y=int(state.y))
        t.write(answer_state)
        # state.state.item => data_frame.series.item in it
        guessed_states.append(answer_state)

# with open("states_to_learn.csv", "w") as file:
#     for state in states:
#         if state not in guessed_states:
#             file.write(f"{state } \n")

screen.exitonclick()