ploiii = int(input("введите площадь прямоугольника: "))


# count = 0
# for i in range(1, ploiii+1):
# 	count += 1 if ploiii % i == 0 else 0
# 	# if ploiii % i == 0:
# 	# 	count += 1
# print('count = ', count//2)




# x=0
# sqrt = int(ploiii**0.5)
# for i in range(1, sqrt+1):
# 	if ploiii % i ==0 :
# 		x+=1  	
# print(x)




# a = set()
# for i in range(1, ploiii+1):
# 	if ploiii % i == 0:
# 		mn = min(i, ploiii//i)
# 		a.add(mn)

# print(len(a))
# print(a)




# a = set()
# for i in range(1, ploiii+1):
# 	if ploiii % i == 0:
# 		arr = sorted([i, ploiii//i])
# 		item = ' '.join(map(str, arr))
# 		print(item)
# 		a.add(item)

# print(len(a))
# print(a)




d = dict()
# d = {}
for i in range(1, ploiii+1):
	if ploiii % i == 0:
		mn = min(i, ploiii//i)
		# if mn not in d.keys():
		d[mn] = max(i, ploiii//i)

print(len(d))
print(d)
