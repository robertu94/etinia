#!/usr/bin/python3

from tkinter import *
from map import Map

world = Map(7, 5)


def key_pressed(event):
    if event.keysym == "Left":
        v.set("Left")
    if event.keysym == "Right":
        v.set("Right")
    if event.keysym == "Up":
        v.set("Up")
    if event.keysym == "Down":
        v.set("Down")

def key_released(event):
    if event.keysym == "Left":
        v.set("Nada")

root = Tk()
root.resizable(width=FALSE, height=FALSE)

v = StringVar()
v.set(str(world))
w = Label(root, textvariable=v, height=24, width=80, bg='black', fg='white', font=("DejaVu Sans Mono", 12))
w.pack()

root.bind_all('<Key>', key_pressed)
root.mainloop()
