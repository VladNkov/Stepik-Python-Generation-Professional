# Снова не успел
# Дан режим работы магазина:
#
# Понедельник	9:00 - 21:00
# Вторник	9:00 - 21:00
# Среда	9:00 - 21:00
# Четверг	9:00 - 21:00
# Пятница	9:00 - 21:00
# Суббота	10:00 - 18.txt:00
# Воскресенье	10:00 - 18.txt:00
# Напишите программу, которая принимает на вход текущие дату и время и определяет количество минут,
# оставшееся до закрытия магазина.
#
# Формат входных данных
# На вход программе подаются текущие дата и время в формате DD.MM.YYYY HH:MM.
#
# Формат выходных данных
# Программа должна вывести количество минут, которое осталось до закрытия магазина, или текст Магазин не работает,
# если он закрыт.


from datetime import datetime, timedelta

schedule = {
    0: ('09:00', '21:00'),
    1: ('09:00', '21:00'),
    2: ('09:00', '21:00'),
    3: ('09:00', '21:00'),
    4: ('09:00', '21:00'),
    5: ('10:00', '18.txt:00'),
    6: ('10:00', '18.txt:00')
}

current_datetime = input()
current_datetime = datetime.strptime(current_datetime, "%d.%m.%Y %H:%M")
current_day = current_datetime.weekday()

open_time, close_time = schedule[current_day]

open_datetime = datetime.strptime(open_time, "%H:%M").replace(year=current_datetime.year,
                                                              month=current_datetime.month, day=current_datetime.day)
close_datetime = datetime.strptime(close_time, "%H:%M").replace(year=current_datetime.year,
                                                                month=current_datetime.month, day=current_datetime.day)

if current_datetime < open_datetime or current_datetime >= close_datetime:
    print("Магазин не работает")
else:
    minutes_until_close = (close_datetime - current_datetime).total_seconds() // 60
    print(int(minutes_until_close))
