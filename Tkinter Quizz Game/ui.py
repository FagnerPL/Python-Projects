from tkinter import *
from quiz_brain import QuizBrain
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
R_IMAGE = os.path.join(BASE_DIR, "true.png")
W_IMAGE = os.path.join(BASE_DIR, "false.png")

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        #main window
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #canvas text
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=290, text="Question", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #Score label
        self.score = Label()
        self.score.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        #Buttons
        right_image = PhotoImage(file=R_IMAGE)
        self.true_button = Button(image=right_image, border=0, bg=THEME_COLOR, command=self.true_answer)
        self.true_button.grid(column=0, row=2)
        wrong_image = PhotoImage(file=W_IMAGE)
        self.false_button = Button(image=wrong_image, bg=THEME_COLOR, border=0, command=self.false_answer)
        self.false_button.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the of the quizz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)



