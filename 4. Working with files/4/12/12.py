import json, csv

with open('students.json', encoding='utf-8') as in_file:
    data = json.load(in_file)
    sorted_data = sorted(data, key=lambda x: x['name'])

with open('data.csv', 'w', encoding='utf-8', newline='') as out_file:
    writer = csv.writer(out_file, delimiter=',')
    writer.writerow(['name', 'phone'])
    for d in sorted_data:
        if int(d['age']) >= 18 and int(d['progress']) >= 75:
            writer.writerow([d['name'], d['phone']])

