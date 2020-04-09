import tkinter as tk
import random as rnd
from init import *


def print_axes(x0, y0, xm, ym, color, canvas):
    canvas.create_line(x0, y0, xm, y0, fill=color, arrow=tk.LAST, dash=(4, 2))
    canvas.create_line(x0, y0, x0, ym, fill=color, arrow=tk.LAST, dash=(4, 2))


def print_dots(n, canvas):
    for _ in range(n):
        x = rnd.randint(pole, w - pole)
        y = rnd.randint(pole, h - pole)
        if x > y:
            fill_color = "#f50"
        else:
            fill_color = "#2f2"
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="#009", fill=fill_color)
