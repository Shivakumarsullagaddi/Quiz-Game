
from tkinter import Label

class Timer:
    def __init__(self, root, seconds, callback):
        self.root = root
        self.seconds = seconds
        self.callback = callback
        self.label = Label(root, text=f"Time left: {self.seconds}s",bg='red',fg='white',font=("times", 12))
        self.label.place(x=10, y=10)
        self.timer_id = None
        self.is_running = False
        self.start_timer()

    def start_timer(self):
        self.is_running = True
        self.update_timer()

    def update_timer(self):
        self.label.config(text=f"Time left: {self.seconds}s")
        if self.seconds > 0 and self.is_running:
            self.timer_id = self.root.after(1000, self.update_timer)
            self.seconds -= 1
        else:
            self.stop_timer()
            self.callback()

    def stop_timer(self):
        self.is_running = False
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
