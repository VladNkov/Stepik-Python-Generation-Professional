import csv


def csv_columns(filename):
    with open(filename, encoding='utf-8') as file:
        data = list(csv.DictReader(file, delimiter=','))

        result_dict = {}
        for row in data:
            for key, value in row.items():
                result_dict.setdefault(key, []).append(value)
    return result_dict


answer = csv_columns('salary_data.csv')
print(answer)