import os
import csv
from utils import *


name_file = 'smartphones.csv'
name_columns = ['name', 'power', 'price']

list_smartphones = get_list_objects(name_file)

list_smartphones.sort(key = lambda obj: obj.price, reverse = True)

list_data = []
list_data.append(name_columns) # добавим заголовки
for item in list_smartphones:
    list_data.append([item.name,item.power,item.price])

file_name, file_extension = os.path.splitext(name_file)
name_file_writer = file_name + '-new' + file_extension
with open(name_file_writer, 'w', newline='') as file:
    writer = csv.writer(file, delimiter = '\t', quoting = csv.QUOTE_NONNUMERIC)
    # for row in list_data:
    #     writer.writerow(row)
    writer.writerows(list_data)

