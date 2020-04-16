class Smart():
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price
    def __repr__(self):
        return '%5d%5d\t%s' % (self.power, self.price, self.name)
