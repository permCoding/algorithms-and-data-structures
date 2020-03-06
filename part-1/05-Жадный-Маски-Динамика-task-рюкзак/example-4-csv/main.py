'''
	поиска максимума - двумерная Динамика
'''
import module as m


arr = m.getArray('input2.csv')  # формируем массив объектов
# for item in arr:  # для контроля данных
# 	print(item)
maxWeight = 100  # ограничение по массе рюкзака
print(m.getMax(arr, maxWeight))  # выводим результат
