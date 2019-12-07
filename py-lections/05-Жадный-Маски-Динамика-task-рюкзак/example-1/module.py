def getLines(fileInput):  # получить все строки файла
	f = open(fileInput, 'r')
	lines = f.read().split('\n')[2:]
	f.close()
	return filter(lambda x: len(x) > 0, lines)


class Item(object):  # декларация класса
	def __init__(self, id, w, p):
		self.id = id
		self.w = w
		self.p = p

	def __repr__(self):
		return '{0}\t{1}'.format(self.w, self.p)


def getArray(lines):  # получить массив объектов
	arr = []
	for line in lines:
		tmp = line.split('\t')
		arr.append(Item(int(tmp[0]), int(tmp[1]), int(tmp[2])))
	return arr


def getMax(arr, maxW):  # жадный алгоритм
	maxP = 0  # найти максимум стоимости
	tmpW = 0  # вес набора
	for elm in arr:
		# print(elm)
		if tmpW + elm.w <= maxW:
			tmpW += elm.w
			maxP += elm.p
	return maxP
