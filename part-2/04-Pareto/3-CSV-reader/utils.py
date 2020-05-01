import csv


class Smart():
    def __init__(self, name, power, price):
        self.name = name
        self.power = power
        self.price = price
    def __repr__(self):
        # return '%5d%5d\t%s' % (self.power, self.price, self.name)
        return '{2}\t{1}\t{0}'.format(self.power, self.price, self.name)


def get_smartphones(file):
    reader = csv.reader(file, delimiter=';')
    list_smartphones = []
    for row in reader:
        try:
            obj = Smart(row[0], int(row[1]), int(row[2]))
            list_smartphones.append(obj)
        except:
            pass
    return list_smartphones


def get_list_objects(name_file):
    list_smartphones = []
    with open(name_file) as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            obj = Smart(row['name'], int(row['power']), int(row['price']))
            list_smartphones.append(obj)
    return list_smartphones
