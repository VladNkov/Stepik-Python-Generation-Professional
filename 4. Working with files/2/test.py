import csv

with open('products.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for line in reader:
        print(*line.values())
        break