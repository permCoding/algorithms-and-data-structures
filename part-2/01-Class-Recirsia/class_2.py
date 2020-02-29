class Animal():
    def __init__(self, h = 10):
        self.height = h

class Human(Animal):
    def __init__(self, name = "Anonym", h = 10):
        self.name = name
        super().__init__(h)

class Ork(Animal):
    def __init__(self, power = 100, h = 10):
        self.power = power
        super().__init__(h)

obj_a = Animal()
print(obj_a.height)

obj_h = Human("Вася")
print(obj_h.height)
print(obj_h.name)

obj_o = Ork(55, 99)
print(obj_o.height)
print(obj_o.power)


