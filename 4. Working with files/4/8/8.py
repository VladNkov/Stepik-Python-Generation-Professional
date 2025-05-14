import json

with open('data1.json', encoding='utf-8') as in_file1:
    data1 = json.load(in_file1)

with open('data2.json', encoding='utf-8') as in_file2:
    data1.update(json.load(in_file2))

with open('data_merge.json', 'w', encoding='utf-8') as file:
    json.dump(data1, file, indent=4, ensure_ascii=False, sort_keys=True)
