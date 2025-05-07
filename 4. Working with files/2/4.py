import csv

with open('salary_data.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))

    data_dict = {}
    for d in data:
        company = d['company_name']
        salary = int(d['salary'])
        data_dict.setdefault(company, []).append(salary)

    avr_salaries = {
        company: sum(salaries)/len(salaries) for company, salaries in data_dict.items()
    }

    print(*sorted(avr_salaries.keys(), key=lambda x: avr_salaries[x]), sep='\n')



