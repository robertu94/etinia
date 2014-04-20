#!/usr/bin/python3

from tkinter import *
from map import Map
from character import Character

world = Map(7, 5)
hero = Character(2, 5)
world.add_unit(hero)
world.add_unit(Character(3,5))
def key_pressed(event):
    if event.keysym == "Left":
        if (world.valid_move(world.units[0].x -1 ,world.units[0].y, world.units[0])):
            world.units[0].move (world.units[0].x-1, world.units[0].y)
    if event.keysym == "Right":
        if (world.valid_move(world.units[0].x +1 ,world.units[0].y, world.units[0])):
            world.units[0].move (world.units[0].x+1, world.units[0].y)
    if event.keysym == "Up":
        if (world.valid_move(world.units[0].x ,world.units[0].y-1, world.units[0])):
            world.units[0].move (world.units[0].x, world.units[0].y -1 )
    if event.keysym == "Down":
        if (world.valid_move(world.units[0].x  ,world.units[0].y+1, world.units[0])):
            world.units[0].move (world.units[0].x, world.units[0].y+1)
    v.set(str(world))


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
