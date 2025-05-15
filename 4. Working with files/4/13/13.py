import json
from datetime import datetime

start_time = datetime.strptime('10:00', '%H:%M').time()
end_time = datetime.strptime('12:00', '%H:%M').time()

with (open('pools.json', encoding='utf-8') as in_file):
    data = json.load(in_file)
    filtered_data = []
    filtered_data1 = []
    answer = 0
    max_length = 0
    max_width = 0
for d in data:
    start_working_time = d['WorkingHoursSummer']['Понедельник'].split('-')[0]
    start_working_time1 = datetime.strptime(start_working_time, '%H:%M').time()
    end_working_time = d['WorkingHoursSummer']['Понедельник'].split('-')[-1]
    end_working_time1 = datetime.strptime(end_working_time, '%H:%M').time()
    if start_working_time1 <= start_time and end_working_time1 >= end_time:
        filtered_data.append(d)

for i in filtered_data:
    if max_length < (int(i['DimensionsSummer']['Length'])):
        max_length = int(i['DimensionsSummer']['Length'])
for i in filtered_data:
    if int(i['DimensionsSummer']['Length']) == max_length:
        filtered_data1.append(i)
for i in filtered_data1:
    if max_width < (int(i['DimensionsSummer']['Width'])):
        max_width = int(i['DimensionsSummer']['Width'])
for i in filtered_data1:
    if int(i['DimensionsSummer']['Width']) == max_width:
        answer = i
# print(answer)
print(f'{answer["DimensionsSummer"]["Length"]}x{answer["DimensionsSummer"]["Width"]}')
print(f'{answer["Address"]}')