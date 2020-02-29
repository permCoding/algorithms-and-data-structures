import random

class Animal():
    count = 0

    def __init__(self, h = 10):
        self.height = h
        self.__class__.count += 1

    def __repr__(self):
        return "Мой рост = {}".format(self.height)

    @staticmethod
    def get_cout():        
        return "Общее кол-во живых = %3d" % Animal.count

lst = []
for i in range(5):
    lst.append( Animal(random.randint(1, 100)) )

print(Animal.count)
print(Animal.get_cout())

for item in lst:
    print(item.height)
    print(item)