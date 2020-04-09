import tkinter as tk
import random as rnd
from init import *


def print_axes(x0, y0, xm, ym, color):
    canvas.create_line(x0, y0, xm, y0, fill=color, arrow=tk.LAST, dash=(4, 2))
    canvas.create_line(x0, y0, x0, ym, fill=color, arrow=tk.LAST, dash=(4, 2))


window = tk.Tk()

canvas = tk.Canvas(window, width=w, height=h, bg='#fda')
canvas.pack()

print_axes(x0, y0, xm, ym, 'blue')

window.mainloop()
