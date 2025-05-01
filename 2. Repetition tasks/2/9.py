size_file = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}
with open('files.txt', 'r', encoding='utf-8') as file:
    data = [line.rstrip().split() for line in file.readlines()]
    data_dict = {}
    for name, size, unit in data:
        ext = name.split('.')[-1]
        size_in_bite = int(size) * size_file[unit]

        if ext not in data_dict:
            data_dict[ext] = []
        data_dict[ext].append((name, size_in_bite))

    for ext in sorted(data_dict.keys()):
        files = sorted(data_dict[ext])
        for name, _ in files:
            print(name)
        print('-'*10)
        total_size = sum(size for _, size in files)
        for unit in ['GB', 'MB', 'KB', 'B']:
            if total_size >= size_file[unit]:
                print(f'Summary:{round(total_size / size_file[unit])} {unit}')
                break
        print()