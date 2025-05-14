import json
import sys

data = json.load(sys.stdin)
for key, value in data.items():
    if type(value) == list:
        print(f'{key}: {", ".join(map(str, value))}')
    else:
        print(f'{key}: {value}')