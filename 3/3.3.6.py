from datetime import datetime

with open('diary.txt', 'r', encoding='utf-8') as file:
    data = file.read().split('\n\n')
    pattern = '%d.%m.%Y; %H:%M'
    data_content = []
    for d in data:
        data_time = datetime.strptime(d[:17], pattern)
        data_text = d[18:]
        data_content.append((data_time, data_text))

    sorted_data_content = sorted(data_content, key=lambda x: x[0].timestamp())
    for data_time, data_text in sorted_data_content:
        print(f'{data_time.strftime(pattern)}\n{data_text}\n')



# for name, (start, end) in data.items():
#     ds_start_time = datetime.strptime(start, pattern).timestamp()
