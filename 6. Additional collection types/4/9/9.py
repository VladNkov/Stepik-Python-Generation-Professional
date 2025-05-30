import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

for animal in data:
    # print(f'name: {animal.name}')
    # print(f'family: {animal.family}')
    # print(f'sex: {animal.sex}')
    # print(f'color: {animal.color}')
    # print()
    for field, value in zip(Animal._fields, animal):
        print(f'{field}: {value}')
    print()
