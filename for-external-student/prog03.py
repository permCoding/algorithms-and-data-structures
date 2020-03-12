'''
    работа с консолью
'''
import sys, math

def ex_1():
    return math.pi

def ex_2():
    return math.pi**2

def ex_3():
    return "%.3f " % math.pi**2

name_function = "ex_" + str(sys.argv[1])

f = globals()[name_function] # из текущего модуля
print('result =', f())

# f = getattr('module', name_function) # из стороннего модуля