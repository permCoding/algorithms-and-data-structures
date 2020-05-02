import csv
# второй способ - через словарь


name_file = 'smartphones.csv'

with open(name_file) as file:
    reader = csv.DictReader(file, delimiter=';')
    for dct in reader:
        # print(dct)
        print(dct['name'], dct['power'], dct['price'])
    

