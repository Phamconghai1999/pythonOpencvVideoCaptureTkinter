import time
import threading
import math
from tkinter import *

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def printTime():
    now = time.strftime("%H:%M:%S %d/%m/%Y")
    clock_lbl.configure(text=now)
    window.after(1000,printTime)

def clicked():
    clock_lbl.configure(text="Click")

window = Tk()
window.title("Clock")
clock_lbl = Label(text="", font=('Helvetica', 20), fg='lime')
clock_lbl.pack()
printTime()

btn1 = Button(text="OK", command=clicked)
btn1.pack(expand=True, side=LEFT, fill=NONE)

window.mainloop()