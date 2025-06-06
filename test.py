from collections import OrderedDict

grades = OrderedDict(Timur=100, Arthur=84, Anri=94, Dima=98)
new_grades = OrderedDict()

for rule in (True, False, False, True):
    name, grade = grades.popitem(last=rule)
    new_grades[name] = grade

print(*new_grades)
