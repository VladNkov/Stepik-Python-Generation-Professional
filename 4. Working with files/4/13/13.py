import json
from datetime import datetime

start_time = datetime.strptime('10:00', '%H:%M').time()
end_time = datetime.strptime('12:00', '%H:%M').time()

with (open('pools.json', encoding='utf-8') as in_file):
    data = list(json.load(in_file))
    filtered_data = []

    for d in data:
        start_working_time = d['WorkingHoursSummer']['Понедельник'].split('-')[0]
        start_working_time = datetime.strptime(start_working_time, '%H:%M').time()
        end_working_time = d['WorkingHoursSummer']['Понедельник'].split('-')[-1]
        end_working_time = datetime.strptime(end_working_time, '%H:%M').time()
        if start_working_time <= start_time and end_working_time >= end_time:
            filtered_data.append((d['Address'], int(d['DimensionsSummer']['Length']), int(d['DimensionsSummer']['Width'])))

    answer = max(filtered_data, key=lambda x: (x[1], x[2]))

print(f'{answer[1]}x{answer[2]}\n{answer[0]}')
# print(f'{answer[0]}')