import module as m

lines = m.getLines('input.txt')
arr = m.getArray(lines)
maxWeight = 100 # ограничение по массе рюкзака


# способ 3 - Генерация наборов битовыми масками
maxPrice = 0
k = len(arr) # кол-во предметов 
# n = 2**k # кол-во наборов
n = 1<<k # кол-во наборов
for i in range(n):
	tmpWeight = 0
	tmpPrice = 0
	for j in range(k):
		mask = 1<<j
		if mask & i > 0:
			tmpWeight += arr[j].w
			tmpPrice += arr[j].p
	if tmpWeight<=maxWeight and tmpPrice>maxPrice:
		maxPrice = tmpPrice

print('maxPrice =', maxPrice)


# перебрать все наборы
#
#	в наборе:
#		найти массу и ценность
#
#	если входит по массе:
#		сравнить максимальную ценность
#