import tkinter as tk
import random as rnd
from init import *
from utils import *

window = tk.Tk()

canvas = tk.Canvas(window, width=w, height=h, bg='#fda')
canvas.pack()

print_axes(x0, y0, xm, ym, 'blue', canvas)

x = rnd.randint(pole, w - pole)
y = rnd.randint(pole, (h - pole)//2)
r = 40  # переопределим сейчас для наглядности
canvas.create_oval(x-r, y-r, x+r, y+r, outline="#00A", fill="#FF0")
canvas.create_oval(x-3, y-3, x+3, y+3, fill="#000")

window.mainloop()
