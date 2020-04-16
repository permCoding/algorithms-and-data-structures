import tkinter as tk
import random as rnd
from init import *


def print_axes(x0, y0, xm, ym, color, canvas):
    '''
        печатает оси координат
    '''
    canvas.create_line(x0, y0, xm, y0, fill=color, arrow=tk.LAST, dash=(4, 2))
    canvas.create_line(x0, y0, x0, ym, fill=color, arrow=tk.LAST, dash=(4, 2))


def print_dots(n, canvas):
    '''
        печатает случайные точки 
        двух цветов в зависимости от координат

    '''
    for _ in range(n):
        x = rnd.randint(pole, w - pole)
        y = rnd.randint(pole, h - pole)
        fill_color = "#f50" if x > y else "#2f2"
        canvas.create_oval(x-r, y-r, x+r, y+r, outline="#009", fill=fill_color)
