import os
import csv
from utils import *


name_file = 'smartphones.csv'
name_columns = ['name', 'power', 'price']

list_smartphones = get_list_objects(name_file)

list_smartphones.sort(key = lambda obj: obj.price, reverse = True)

file_name, file_extension = os.path.splitext(name_file)
name_file_writer = file_name + '-new' + file_extension

with open(name_file_writer, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames = name_columns)
    writer.writeheader()
    for obj in list_smartphones:
        dct = dict.fromkeys(name_columns)
        dct['name'] = obj.name
        dct['power'] = obj.power
        dct['price'] = obj.price
        writer.writerow(dct)

# pass
