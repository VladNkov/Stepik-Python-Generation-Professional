import json, csv

with open('playgrounds.csv', encoding='utf-8') as in_file, open('addresses.json', 'w') as our_file:
    data = list(csv.DictReader(in_file, delimiter=';'))
    addresses = {}

    for d in data:
        addresses.setdefault(d['AdmArea'], {}).setdefault(d['District'], []).append(d['Address'])

    json.dump(addresses, our_file, indent=4, ensure_ascii=False)

