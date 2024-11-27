from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("Main Window")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("Top Level")
    l2 = Label(top, text="This is the top-level window")
    l2.pack()

l = Label(root, text="This is the root window")
l.pack()

btn = Button(root, text="Click here to open another window", command=topwin)
btn.pack()

root.mainloop()
