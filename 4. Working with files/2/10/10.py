import csv
from datetime import datetime

pattern = '%d/%m/%Y %H:%M'

with open('name_log.csv', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=','))

data_dict = {}

for d in data:
    username, email = d['username'], d['email']
    dtime = datetime.strptime(d['dtime'], '%d/%m/%Y %H:%M')

    if email not in data_dict or dtime > data_dict[email]['dtime']:
        data_dict[email] = {'username': d['username'], 'dtime': dtime}

sorted_logs = sorted(data_dict.items(), key=lambda x: x[0])
print(sorted_logs)

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as write_file:
    writer = csv.writer(write_file, delimiter=',')
    writer.writerow(['username', 'email', 'dtime'])
    for email, username_data in sorted_logs:
        writer.writerow([username_data['username'], email, username_data['dtime'].strftime('%d/%m/%Y %H:%M')])

