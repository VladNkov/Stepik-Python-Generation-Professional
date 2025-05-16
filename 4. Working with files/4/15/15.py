import json

with open('food_services.json', encoding='utf-8') as in_file:
    data = list(json.load(in_file))
    operating_company = []
    companies_dict = {}
    objects_in_district = {}

    for d in data:
        objects_in_district.setdefault(d['District'], []).append(d['Name'])

    answer1 = max(objects_in_district.items(), key=lambda x: len(x[1]))
    print(f'{answer1[0]}: {len(answer1[1])}')

    for d in data:
        if d['IsNetObject'] == 'да':
            operating_company.append(d)

    for o in operating_company:
        companies_dict.setdefault(o['OperatingCompany'],[]).append(o['Name'])

    answer2 = max(companies_dict.items(), key=lambda x: len(x[1]))
    print(f'{answer2[0]}: {len(answer2[1])}')