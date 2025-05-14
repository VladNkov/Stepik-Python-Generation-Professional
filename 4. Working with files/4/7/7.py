import json

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)
    new_data = []

for d in data:
    if isinstance(d, str):
        new_data.append(d+'!')
    elif isinstance(d, bool):
        new_data.append(not d)
    elif isinstance(d, int):
        new_data.append(d + 1)
    elif isinstance(d, list):
        new_data.append(d+d)
    elif isinstance(d, dict):
        d["newkey"] = None
        new_data.append(d)
    elif d is None:
        continue
for i in new_data:
    print(i)

with open('updated_data.json', 'w', encoding='utf-8') as file:
    json.dump(new_data, file, indent=4, ensure_ascii=False)