from tkinter import *
import time

class Clock():
    def __init__(self):
        self.root = Tk()
        self.label = Label(text="", font=('Helvetica', 48), fg='lime')
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S %d-%m-%Y")
        self.label.configure(text=now)
        self.root.after(1000, self.update_clock)

app=Clock()