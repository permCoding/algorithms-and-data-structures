import csv  # CSV - Comma Separated Values - Значения, Разделенные Запятыми
# читаем csv и сразу выводим
# pip3 install csv


def print_data(file):
    reader = csv.reader(file, delimiter = ';')
    for row in reader:
        # print(row) # список
        print(' '.join(row))


name_file = 'smartphones.csv'

list_smartphones = []
with open(name_file, 'r') as file:
    print_data(file)

pass
