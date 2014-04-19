#!/usr/bin/python3

from tkinter import *

def keyPressed(event):
    if(event.keysym == "Left"):
        v.set("Left")
    if(event.keysym == "Right"):
        v.set("Right")
    if(event.keysym == "Up"):
        v.set("Up")
    if(event.keysym == "Down"):
        v.set("Down")

def keyReleased(event):
    if(event.keysym == "Left"):
        v.set("Nada")

root = Tk()
root.resizable(width=FALSE, height=FALSE)

v = StringVar()
v.set("This is a super long starting string that \nwon't possibly fit but is instead a test to see how tkinter handles wrapping\nWow that was just a \\n. Amazing!")
w = Label(root, textvariable=v, height=24, width=80, bg="black", fg="white", font=("DejaVu Sans Mono", 12))
w.pack()

root.bind_all('<Key>', keyPressed)
root.mainloop()
