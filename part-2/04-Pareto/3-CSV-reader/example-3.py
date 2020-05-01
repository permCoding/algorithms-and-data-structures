import csv
# второй способ - через словарь


name_file = 'smartphones.csv'

with open(name_file) as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        # print(row)
        print(row['name'], row['power'], row['price'])
    

