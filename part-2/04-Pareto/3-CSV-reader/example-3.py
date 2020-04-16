import csv


name_file = 'smartphones.csv'
with open(name_file) as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        print(row['name'], row['power'], row['price'])
    

