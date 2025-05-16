import json

with open('food_services.json', encoding='utf-8') as in_file:
    data = list(json.load(in_file))
    type_object = {}
    answer = []

    for d in data:
        type_object.setdefault(d['TypeObject'], []).append((d['Name'], int(d['SeatsCount'])))

    for type_name, name_seats in sorted(type_object.items()):
        largest = max(name_seats, key=lambda x: x[1])
        answer.append(f'{type_name}: {largest[0]}, {largest[1]}')
    for a in answer:
        print(a)
