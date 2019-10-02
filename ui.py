import tkinter
from tkinter.constants import *

def show_opt():

    tk = tkinter.Tk()

    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH, expand=1)

    # Take a picture button:
    label = tkinter.Label(frame, text="Take a picture: ")
    label.pack(fill=X, expand=1)
    button = tkinter.Button(frame, text="Snap!", command=tk.destroy)
    button.pack(side=BOTTOM)

    tk.mainloop()

show_opt()