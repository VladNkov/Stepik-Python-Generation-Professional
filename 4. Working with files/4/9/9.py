import json

with open('people.json', encoding='utf-8') as in_file, open('updated_people.json', 'w') as out_file:
    data = json.load(in_file)
    keys_list = []

for items in data:
    for key in items.keys():
        if key not in keys_list:
            keys_list.append(key)

for items in data:
    for key in keys_list:
        items.setdefault(key)

json.dump(data, out_file, ensure_ascii=False, indent=4)
