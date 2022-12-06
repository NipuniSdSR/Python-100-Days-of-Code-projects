from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        # Label
        self.score_label = Label(text=f"Score : 0", padx=20, pady=20, highlightthickness=0, bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=0)
        # Canvas text
        self.canvas_text = self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text=f"some text",
                                                   font=("Arial", 20, "italic"),
                                                   fill="black")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score : {self.quiz.score}")

        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.canvas_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
