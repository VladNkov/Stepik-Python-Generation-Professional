import csv

with open('deniro.csv', encoding='utf-8') as file:
    data = list(csv.reader(file))

n = int(input())-1

sorted_data = sorted(data, key=lambda x: float(x[n]) if x[n].isdigit() else x[n])

for d in sorted_data:
    print(*d, sep=',')





