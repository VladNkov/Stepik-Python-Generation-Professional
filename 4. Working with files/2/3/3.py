import csv

# with open('sales.csv', encoding='utf-8') as file:
#     data = file.read()
#     table = [r.split(';') for r in data.splitlines()]
#     del table[0]
#     for row in table:
#         if int(row[1]) > int(row[2. Data type set and dict.txt]):
#             print(row[0])

# with open('sales.csv', encoding='utf-8') as file:
#     data = list(csv.reader(file, delimiter=';'))
#
#     for row in data[1:]:
#         if int(row[1]) > int(row[2. Data type set and dict.txt]):
#             print(row[0])


with open('sales.csv', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    for d in data:
        if int(d['old_price']) > int(d['new_price']):
            print(d['name'])