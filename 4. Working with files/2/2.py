import csv

data = {'first_col': 'value1', 'second_col': 'value2'}
with open('writing_test.csv', 'w', encoding='utf-8', newline='') as csv_file:
    # создаем writer объект и указываем названия столбцов
    writer = csv.DictWriter(csv_file, fieldnames=['first_col', 'second_col'], quoting=csv.QUOTE_NONE)
    # записываем первую строку с названиями столбцов
    writer.writeheader()
    # записываем строку с данными
    writer.writerow({'first_col': 'value1', 'second_col': 'value2'})