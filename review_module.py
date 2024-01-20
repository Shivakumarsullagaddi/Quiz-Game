from tkinter import Toplevel,Button, Scrollbar, Text, END
from tkinter import WORD

class ReviewModule:
    def __init__(self, root, questions, correct_answers, user_answers):
        self.root = root
        self.questions = questions
        self.correct_answers = correct_answers
        self.user_answers = user_answers
        
    def show_review(self):
        review_window = Toplevel(self.root)
        review_window.title("Review Answers")
        text_widget = Text(review_window, wrap=WORD, width=60, height=20, font=("times", 12))
        text_widget.pack(padx=10, pady=10)

        for i in range(len(self.questions)):
            question_text = f"Q: {self.questions[i]}\n"
            correct_answer_text = f"Correct Answer: {self.correct_answers[i]}\n"
            user_answer_text = f"Your Answer: {self.user_answers[i]}\n\n"
            text_widget.insert(END, question_text)
            text_widget.insert(END, correct_answer_text)
            text_widget.insert(END, user_answer_text)
        close_button = Button(review_window, text="Close", command=review_window.destroy)
        close_button.pack(pady=10)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #     for i in range(min(len(self.questions), len(self.user_answers))):
    # question_text = f"Question : {self.questions[i]}\n"
    # correct_answer_text = f"Correct Answer: {self.correct_answers[i]}\n"
    
    # # Check if the index is within the range of user answers
    # if i < len(self.user_answers):
    #     user_answer_text = f"Your Answer: {self.user_answers[i]}\n\n"
    # else:
    #     user_answer_text = "Your Answer: [Not Attempted]\n\n"

    # review_label = Label(review_window, text=question_text + correct_answer_text + user_answer_text)
    # review_label.pack()