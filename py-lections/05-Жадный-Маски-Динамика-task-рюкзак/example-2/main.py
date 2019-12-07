import module as m

lines = m.getLines('input.txt')
arr = m.getArray(lines)
maxWeight = 100 # ограничение по массе рюкзака


# способ 2 - Рекурсивная генерация наборов
tmp = []
maxPrice = 0
def getSubsets(k):
	global tmp
	global maxPrice
	if k == len(arr):
		print(*tmp)
		# дописать проверку
	else:
		tmp.append(arr[k])
		getSubsets(k+1)
		tmp.pop()
		getSubsets(k+1)

getSubsets(0)

print('maxPricerice =', maxPrice)
