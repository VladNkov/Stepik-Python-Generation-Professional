import csv
from datetime import datetime, date, time

with open('meetings.csv', encoding='utf-8') as csv_file:
    data_list = list(csv.DictReader(csv_file, delimiter=','))
    data_dict = {}
    for d in data_list:
        meeting_date_str = d['meeting_date'] + ' ' + d['meeting_time']
        meeting_date = (datetime.strptime(meeting_date_str, '%d.%m.%Y %H:%M'))
        surname, name = d['surname'], d['name']
        data_dict[f'{surname} {name}'] = meeting_date
    sorted_dict = sorted(data_dict.items(), key=lambda x: x[1])
    for full_name, meeting_date in sorted_dict:
        print(f'{full_name}')

