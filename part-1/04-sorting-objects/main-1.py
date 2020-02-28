# x = input()
# print(dir(x))
# print(x.strip())
# print(x.capitalize())

import copy


class Point():
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return "{0}\t{1}".format(self.x, self.y)


class Line():
	def __init__(self, a, b):
		self.pointA = a
		self.pointB = b

	def getLength(self):
		return ((self.pointA.x-self.pointB.x)**2 + (self.pointA.y-self.pointB.y)**2)**.5


point_1 = Point()
# point_1.x = 0
# point_1.y = 0

point_2 = Point(3, 4)
# point_2.x = 3
# point_2.y = 4

point_3 = copy.copy(point_2)
point_3.x = 2

line = Line(point_1, point_2)
print(line.getLength())

arr = [point_1, point_2, point_3]
print(arr)
print(*arr)

for obj in arr:
	print(obj)

newArr = sorted(arr, key=lambda elm: elm.x)
for obj in newArr:
	print(obj)

arr.sort(key=lambda elm: elm.x, reverse=True)
for obj in arr:
	print(obj)
