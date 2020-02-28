import module as m

lines = m.getLines('input2.txt')
arr = m.getArray(lines)
maxWeight = 100 # ограничение по массе рюкзака


# способ 4 - Динамика
tab = []
for i in range(maxWeight+1): # [w,p]
	row = [ [0,0] for i in range(len(arr)) ]
	tab.append(row)

col = 0
for row in range(maxWeight+1):
	if row >= arr[col].w:
		tab[row][col] = [arr[col].w,arr[col].p]

for row in range(maxWeight+1):
	for col in range(1,len(arr)):
		v1 = tab[row][col-1]
		v2 = tab[row-arr[col].w][col-1]
		if v2[0]+arr[col].w <= row and v2[1]+arr[col].p > v1[1]:
			tab[row][col] = [v2[0]+arr[col].w,v2[1]+arr[col].p]
		else:
			tab[row][col] = v1

print(tab[maxWeight][len(arr)-1])









# print('maxPrice =', maxPrice)