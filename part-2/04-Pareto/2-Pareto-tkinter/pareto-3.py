import tkinter as tk
from init import *
from utils import *

window = tk.Tk()

canvas = tk.Canvas(window, width=w, height=h, bg='#fda')
canvas.pack()

print_axes(x0, y0, xm, ym, 'blue', canvas)
count_dots = 250  # кол-во точек будет определяться данными
# тут можно сделать загрузку данных из файла
print_dots(count_dots, canvas)

window.mainloop()
