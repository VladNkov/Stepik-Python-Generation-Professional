import calendar, locale


print(*[calendar.isleap(int(input())) for i in range(int(input()))])
