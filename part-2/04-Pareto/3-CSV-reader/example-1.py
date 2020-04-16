import csv  # CSV - Comma Separated Values - Значения, Разделенные Запятыми

def csv_reader(file):
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        print(' '.join(row))


name_file = 'smartphones.csv'
list_smartphones = []
with open(name_file, 'r') as file:
    csv_reader(file)
