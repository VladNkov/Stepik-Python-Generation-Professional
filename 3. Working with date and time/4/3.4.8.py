from datetime import date, time, timedelta, datetime

date_list = input().split()
date_list1 = list(map(lambda x: datetime.strptime(x, '%d.%m.%Y'), date_list))
list2 = []
for i in range(len(date_list1)):
    if i+1 < len(date_list1):
        list2.append(abs(date_list1[i] - date_list1[i+1]).days)
    else:
        break
print(list2)