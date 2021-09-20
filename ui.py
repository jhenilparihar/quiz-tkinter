import tkinter
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tkinter.Tk()
        self.window.title('Quiz')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.iconbitmap("images/icon.ico")
        self.window.attributes('-alpha', 0.96)
        self.window.resizable(False, False)
        self.label = tkinter.Label(text='Score: 0', bg=THEME_COLOR, fg='white', font=('Arial', 15, 'normal'))
        self.label.grid(column=1, row=0)
        self.canvas = tkinter.Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text='QUiz Question Goes Here', fill=THEME_COLOR,
                                                     width=280,
                                                     font=('Arial', 15, 'italic'))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = tkinter.PhotoImage(file='images/true.png')
        self.true = tkinter.Button(image=self.true_img, highlightthickness=0, border=0, command=self.clicked_true)
        self.true.grid(column=0, row=2)

        self.false_img = tkinter.PhotoImage(file='images/false.png')
        self.false = tkinter.Button(image=self.false_img, highlightthickness=0, border=0, command=self.clicked_false)
        self.false.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        self.label.config(text=f"Score : {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You Have Completed The Quiz')
            self.true.config(state='disable')
            self.false.config(state='disable')

    def clicked_true(self):
        self.feedback(self.quiz.check_answer('true'))

    def clicked_false(self):
        self.feedback(self.quiz.check_answer('false'))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg='red')
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)
