import json

with open('countries.json', encoding='utf-8') as in_file:
    data = json.load(in_file)


religions = {}
for i in data:
    country = i['country']
    religion = i['religion']
    religions.setdefault(religion, []).append(country)


with open('religion.json', 'w') as out_file:
    json.dump(religions, out_file, indent=4)