from tkinter import *
from time import strftime

root = Tk()
root.title("CLOCK")


# time function
def time():
    str = strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000, time)


# display
label = Label(root, font=("HElvetica", 80), bg="black", fg="cyan")
label.pack(anchor='center')

time()

mainloop()