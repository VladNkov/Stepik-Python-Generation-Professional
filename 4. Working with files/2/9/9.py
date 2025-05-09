import csv

with open('titanic.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))
    data_dict = {}
    for d in data:
        survived, name, sex, age = int(d['survived']), d['name'], d['sex'], float(d['age'])
        if survived != 0 and age < 18:
            data_dict.setdefault(name, []).append(sex)

    for items in data_dict:
        sorted_data = sorted(data_dict.items(), key=lambda x: x[1], reverse=True)
    for name, sex in sorted_data:
        print(name)
