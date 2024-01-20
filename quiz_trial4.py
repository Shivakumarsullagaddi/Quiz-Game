from tkinter import *
from tkinter import messagebox as mb
from timer_module import Timer
import json
from hint_module import Hint
from background_module import Background
from review_module import ReviewModule
from tkinter import Tk, Button
from replay_module import ReplayModule
import python_logo
from tkinter import messagebox

root = Tk()
background = Background(root)
label = Label(background)
label=Label(root)
logo =PhotoImage(file='python.gif')
small_logo=logo.subsample(2,2)
label.config(image=small_logo) 
label.config(compound='bottom')
label.place(x=730, y=43)

root.geometry("800x500")
root.title("Quiz")
with open('quiz.json') as f:
    obj = json.load(f)
    q = obj['ques']
    a = obj['ans']
options = obj['options']

class Quiz:
    def __init__(self, root, correct_count, total_questions, questions, user_answers):
        self.root = root
        self.qn = 0
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0
        self.hint_module = Hint(root, "", 0)
        self.user_answers = user_answers
        self.review_module = ReviewModule(root, q, a, self.user_answers)
        self.total_questions = total_questions
        self.questions = questions
        self.user_answers = user_answers
        self.replay_module = ReplayModule(root, self.replay_callback)
        
    def question(self, qn):
        t = Label(root, text="Quiz in Python Programming", width=50, bg="blue", fg="white", font=("A", 20, "bold"))
        t.place(x=0, y=2)
        qn = Label(root, text=q[qn], width=60, font=("times", 16, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn
    
    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("times", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b
    
    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]

        for idx, op in enumerate(options[qn]):
            btn = self.opts[val]
            btn['text'] = op
            btn.config(bg="SystemButtonFace") 
            btn.config(command=lambda v=idx + 1: self.check_and_color(v, qn))
            val += 1

    def check_and_color(self, user_answer, qn):
        is_correct = user_answer == a[qn]
        color = "green" if is_correct else "red"
        self.opts[user_answer - 1].config(bg=color)

    def start_timer(self):
        self.timer = Timer(root, 60, self.nextbtn)

    def nextbtn(self):
        if 0 < self.timer.get_seconds() <= 6:
            user_answer = self.opt_selected.get()
            correct_answer = a[self.qn]
            is_correct = user_answer == correct_answer
            color = "green" if is_correct else "red"
            self.opts[correct_answer - 1].config(bg=color)
        super().nextbtn()

    def buttons(self):
        nbutton = Button(self.root, text="Next", command=self.nextbtn, width=10,
                         bg="green", fg="white", font=("times", 16, "bold"))
        nbutton.place(x=200, y=380)

        hint_button = Button(self.root, text="Hint", command=self.show_hint, width=10,
                             bg="yellow", fg="black", font=("times", 16, "bold"))
        hint_button.place(x=320, y=380)

        quitbutton = Button(self.root, text="Quit", command=self.root.destroy, width=10,
                            bg="red", fg="white", font=("times", 16, "bold"))
        quitbutton.place(x=440, y=380)
        
    def checkans(self, qn):
        if 0 <= qn < len(a):
            user_answer = self.opt_selected.get()
            self.user_answers.append(user_answer)  
            correct_answer = a[qn]
            is_correct = user_answer == correct_answer
            self.opts[correct_answer - 1].config(bg="green" if is_correct else "red")

            return is_correct
        else:
            print("Invalid question index for answer.")
            return False
    
    def nextbtn(self):
        self.timer.stop_timer()
        if self.checkans(self.qn):
            self.correct += 1
        self.user_answers.append(self.opt_selected.get())
        self.qn += 1
        if self.qn == len(q):
            self.display_result()
            self.review_module = ReviewModule(root, self.correct, len(q), q, self.user_answers)
        else:
            self.display_options(self.qn)
            self.timer = Timer(root, 60, self.nextbtn)

    def display_result(self):
        self.timer.stop_timer()  
        score = int(self.correct / len(q) * 100)
        result = "Score: " + str(score) + "%"
        wc = len(q) - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))
        self.show_review_button()
        self.show_replay_button()
        
    def show_review_button(self):
        review_button = Button(self.root, text="SOLUTION", command=self.show_review, width=15,
                            bg="blue", fg="white", font=("times", 16, "bold"))
        review_button.place(x=200, y=450)
              
    def show_review(self):        
        self.review_module = ReviewModule(root, q, a, self.user_answers)
        self.review_module.show_review()
        
    def show_hint(self):
        hint_texts = [
            "Special symbol for comments in Python is among 1 and 4",
            "Syntax error is detected by among 2 and 4",
            "Operator with the highest precedence is 3 and 4",
            "The format function returns a formatted 1 and 3",
            "Correct statement: among 1 and 2"
        ]
        if 0 <= self.qn < len(hint_texts):
            current_hint_text = hint_texts[self.qn]
            correct_option = a[self.qn]
            hint_module = Hint(self.root, current_hint_text, correct_option)
            hint_module.show_hint()
        else:
            messagebox.showwarning("Invalid Question Index", "No hint is available")
            
    def show_replay_button(self):
        replay_module = ReplayModule(self.root, self.replay_callback)

    def replay_callback(self):
        self.qn = 0
        self.correct = 0
        self.user_answers = []
        self.display_options(self.qn)
        self.timer = Timer(root, 60, self.nextbtn)
        self.replay_module.hide_replay_button()
        
    def show_replay_button(self):
        replay_button = Button(self.root, text="RE ATTEMPT", command=self.ask_replay, width=14,
                                bg="green", fg="white", font=("times", 16, "bold"))
        replay_button.place(x=390, y=450)

    def ask_replay(self):
        replay = mb.askquestion("Replay", "Do you want to play again?")

        if replay == "yes":
            self.replay_callback()
        else:
            print('nothing')
            
quiz = Quiz(root, 0, len(q), q, [])
quiz.start_timer()
quiz.timer = Timer(root, 60, quiz.nextbtn)
root.mainloop()





