import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    timer_label.config(text="Timer")
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# Todo: 6.tie start_timer function to start button

# repition needs to happen every 8 ful set.
# 1.3.5.7: are work min
# 2, 4, 6 : breaks
# 8 : longer break
def start_timer():
    global reps
    reps += 1

    work_sec = 5#WORK_MIN * 60
    short_break_sec = 2#SHORT_BREAK_MIN * 60
    long_break_sec = 3#LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


# Todo: 5. set up the timer.
# use buildin function 'after' which activeate given function after given milli seconds
# to amend the items in the canvas we called itemconfig of canvas class

def count_down(count):
    global timer

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        # Todo: 7 Adjust the check mark according to the full work session. v for work

        marks = ""
        start_timer()

        work_sessions = math.floor(reps/2)

        # print(f"{work_sessions}:{reps}")
        for _ in range(work_sessions):
            marks += "✓"
            check_label.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
# Todo: 1. setup the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)
# change the background of the window to yellow


# canvas drawing surface widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# change the background of the canvas, the margin still show in white, make the 'highlightthickness' =0

# Todo: 2. setup the image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Todo: 3 setup the timer label
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Todo: 4. create a label
# fg: foreground color to change the color of the font
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

check_label = Label(text="", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# Todo: 5. create buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
