import csv

with open('wifi.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))

    distr_dict = {}
    for d in data:
        district, num_points = d['district'], int(d['number_of_access_points'])
        distr_dict[district] = distr_dict.get(district, 0) + num_points

sorted_dict = sorted(distr_dict.items(), key=lambda x: (-x[1], x[0]))
for district, count in sorted_dict:
    print(f'{district}: {count}')


