import tkinter as tk
from init import *


window = tk.Tk()

canvas = tk.Canvas(window, width=w, height=h, bg='#fda')
canvas.pack()

canvas.create_line(x0, y0, xm, y0, fill="#000", arrow=tk.LAST, dash=(6, 2))

window.mainloop()
