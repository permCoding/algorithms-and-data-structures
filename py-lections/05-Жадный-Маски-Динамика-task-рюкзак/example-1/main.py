import module as m

lines = m.getLines('input.txt')
arr = m.getArray(lines)
maxW = 100  # ограничение по массе


# способ 1 - Жадный алгоритм

# способ 1 - именованная функция
def getAttr(obj):
	return obj.p/obj.w


arr.sort(key=getAttr, reverse=True)

# способ 2 - импорт модуля
# from operator import attrgetter
# arr.sort(key = attrgetter('p'), reverse = True)

# способ 3 - анонимная функция
# arr.sort(key = lambda x : x.p, reverse = True)
# arr.sort(key = lambda x : x.p/x.w, reverse = True)

print('maxPrice =', m.getMax(arr, maxW))


# способ 2 - Рекурсивная генерация наборов
# способ 3 - Бинарные маски
# способ 4 - Динамика
