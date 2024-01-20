from tkinter import Button

class ReplayModule:
    def __init__(self, root, replay_callback):
        self.root = root
        self.replay_callback = replay_callback

    def show_replay_button(self):
        self.replay_button.pack()

    def hide_replay_button(self):
        self.replay_button.pack_forget()
