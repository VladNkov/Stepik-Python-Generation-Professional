import csv
from datetime import datetime, date, time
from collections import namedtuple

with open('meetings.csv', encoding='utf-8') as file:
    header, *data = csv.reader(file)

    Friend = namedtuple('Friend', ['ful_name', 'datetime'])
    friends = []
    pattern = '%d.%m.%Y %H:%M'
    # print(data)

    for d in data:
        friends.append(Friend(f'{d[0]} {d[1]}', datetime.strptime(f'{d[2]} {d[3]}', pattern)))
    # print(friends)

    for friend in sorted(friends, key=lambda x: x.datetime):
        print(friend.ful_name)