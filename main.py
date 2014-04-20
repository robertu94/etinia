#!/usr/bin/python3

from tkinter import *
from map import Map
from character import Character
from mapcontroller import MapController

world = Map(7, 5)
hero = Character(0,2, 5, team=1)
world.add_unit(hero)
world.add_unit(Character(1, 3, 5))
map_controller = MapController(world)


def key_pressed(event):
    map_controller.move(event.keysym)
    v.set(str(world))

root = Tk()
root.resizable(width=FALSE, height=FALSE)

v = StringVar()
v.set(str(world))
w = Label(root, textvariable=v, height=24, width=80, bg='black', fg='white', font=("DejaVu Sans Mono", 12))
w.pack()

root.bind_all('<KeyPress>', key_pressed)
root.mainloop()
