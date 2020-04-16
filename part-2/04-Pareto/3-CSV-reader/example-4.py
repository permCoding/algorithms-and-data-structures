import csv
from utils import *


def get_smartphones(file):
    reader = csv.reader(file, delimiter=';')
    lst = []
    for row in reader:
        try:
            obj = Smart(row[0], int(row[1]), int(row[2]))
            lst.append(obj)
        except:
            pass
    return lst


list_smartphones = []
name_file = 'smartphones.csv'
with open(name_file) as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        obj = Smart(row['name'], int(row['power']), int(row['price']))
        list_smartphones.append(obj)

for item in list_smartphones:
    print(item)
