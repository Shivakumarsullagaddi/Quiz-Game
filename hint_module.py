from tkinter import messagebox

class Hint:
    def __init__(self, root, hint_text, correct_option):
        self.root = root
        self.hint_text = hint_text
        self.correct_option = correct_option

    def show_hint(self):
        hint_message = f"{self.hint_text}"
        messagebox.showinfo("Hint", hint_message)

    def disable_incorrect_options(self):
        for i in range(1, 5):
            if i != self.correct_option:
                self.root.opts[i - 1]['state'] = 'disabled'









