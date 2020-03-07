import csv


class Item(object):  # декларация класса
	def __init__(self, id, w, p):
		self.id = id
		self.w = w
		self.p = p

	def __repr__(self):
		return '{0}\t{1}\t{2}'.format(self.id, self.w, self.p)

def getArray(name_file):  # получить массив объектов из csv-файла
	arr = []
	with open(name_file, 'r') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=';', quotechar='\n')
		for row in reader:  # row - словарь
			arr.append(Item(int(row['id']),int(row['w']),int(row['p'])))
	return arr


def getMax(arr, maxWeight):
	# инициализируем таблицу для хранения динамики
	tab = []
	for _ in range(maxWeight+1):  # [w,p]
		row = [[0, 0] for i in range(len(arr))]
		tab.append(row)  # одна строка в таблице

	# формируем левый столбец
	col = 0
	for row in range(maxWeight+1):
		if row >= arr[col].w:
			tab[row][col] = [arr[col].w, arr[col].p]

	# заполняем таблицу
	for row in range(maxWeight+1):
		for col in range(1, len(arr)):
			v1 = tab[row][col-1]
			v2 = tab[row-arr[col].w][col-1]
			if v2[0]+arr[col].w <= row and v2[1]+arr[col].p > v1[1]:
				tab[row][col] = [v2[0]+arr[col].w, v2[1]+arr[col].p]
			else:
				tab[row][col] = v1

	return tab[maxWeight][len(arr)-1]  # результат в крайней ячейке
