from collections import defaultdict


def flip_dict(data):
    d_dict = defaultdict(list)
    for key, value in data.items():
        for v in value:
            d_dict[v].append(key)

    return d_dict


print(flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]}))

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')