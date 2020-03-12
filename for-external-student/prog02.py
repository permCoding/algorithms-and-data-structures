'''
    работа с консолью
'''

import sys
import os
import platform


def cls_screen():
    name_os = platform.system()
    cmd_clear = "clear" if name_os == "Linux" else "cls"
    os.system(cmd_clear) # очистка экрана

cls_screen()

arr = sys.argv[1:] # параметры из командной строки

print(arr)
print(*arr)

print('sum =', sum(list(map(int, arr))))
print('sum =', max(list(map(int, arr))))
