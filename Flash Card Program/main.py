from tkinter import *

import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ----------------------RANDOM WORD GENERATOR---------------#
# Todo: 4.Reading csv word_set
try:
    data_frame = pandas.read_csv("./data/learning_set.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("./data/french_words.csv")

word_set = data_frame.to_dict(orient="records")


current_card = {}


# Todo: 5.Show the next card_background when any button is clicked
def next_card():
    global flip_timer
    global current_card

    # Todo: 9 cancel flipping before jumping to next card
    window.after_cancel(flip_timer)

    # -------------------------#

    current_card = random.choice(word_set)

    canvas.itemconfig(card_background, image=front_card_image)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    # Todo: 7.Flip the card_background after 3s
    flip_timer = window.after(3000, flip_card)


# ----------------------FLIP THE CARD-----------------------#

def flip_card():
    canvas.itemconfig(card_background, image=back_card_image)

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# ----------------------PROGRESS SAVING-----------------------#
# Todo: 10. Save the words that missed and save them to csv file
def words_to_learn():
    word_set.remove(current_card)
    learning_dataset = pandas.DataFrame(word_set)
    print(len(learning_dataset))
    # to_csv command overwrite the existing file
    learning_dataset.to_csv("./data/learning_set.csv", index=False)

    next_card()


# ----------------------UI SETUP----------------------------#

# Todo: 1. Tk window
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

# Todo: 8 Initial card flip timer
flip_timer = window.after(3000, flip_card)

# Todo: 2. Canvas and the flash card_background image on it
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")

card_background = canvas.create_image(400, 263, image=front_card_image)

# # Todo:4. texts on the canvas
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 253, text="", font=("Ariel", 60, "bold"), fill="black")

canvas.grid(column=0, row=0, columnspan=2)

# # Todo: 3. Buttons
check_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=check_image, highlightthickness=0, command=next_card)
correct_button.grid(column=0, row=1)

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=words_to_learn)
wrong_button.grid(column=1, row=1)

# # Todo: 6. Initial card_background display:after canvas was created:
next_card()

window.mainloop()
