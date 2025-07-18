from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]

data_dict = defaultdict(int)
for item, value in data:
    data_dict[item] += value
sorted_dict = sorted(data_dict.items(), key=lambda x: x[0])
for item, value in sorted_dict:
    print(f'{item}: ${value}')