arr = [
	'100 Абрикосов',
	'99 Виноградов',
	'1 Персиков'
]


arr.sort(key=lambda item: int(item.split()[0]), reverse=True)
for obj in arr:
	print(obj)

print()

arr.sort(key=lambda item: int(item.split()[0]))
for obj in arr:
	print(obj)

print()

arr.sort(key=lambda item: item.split()[1], reverse=True)
for obj in arr:
	print(obj)
