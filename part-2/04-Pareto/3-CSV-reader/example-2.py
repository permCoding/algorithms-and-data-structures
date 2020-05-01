import csv
from utils import *
# читаем csv, формируем объекты, размещаем в список


name_file = 'smartphones.csv'

list_smartphones = []
with open(name_file, 'r') as file:
    list_smartphones = get_smartphones(file)

for item in list_smartphones:
    print(item)
