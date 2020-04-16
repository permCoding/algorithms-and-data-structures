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


name_file = 'smartphones.csv'
list_smartphones = []
with open(name_file, 'r') as file:
    list_smartphones = get_smartphones(file)

for item in list_smartphones:
    print(item)
