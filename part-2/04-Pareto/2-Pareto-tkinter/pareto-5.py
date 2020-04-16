import tkinter as tk
from init import *
from utils import *

def worker():
    print_dots(count_dots, canvas)

window = tk.Tk()
count_dots = 250  # назначим количество точек
canvas = tk.Canvas(window, width=w, height=h, bg='#fda')

btn_start = tk.Button(window,
    text='Pareto',
    width=15,
    command=worker
)

# btn_start = tk.Button(window,
#     text='Pareto',
#     width=15,
#     command=lambda: print_dots(count_dots, canvas)
# )

btn_start.pack()
canvas.pack()
print_axes(x0, y0, xm, ym, 'blue', canvas)
window.mainloop()
