import csv
from utils import *
# словарь, функция, модуль


name_file = 'smartphones.csv'

list_smartphones = get_list_objects(name_file)

for item in list_smartphones:
    print(item)
