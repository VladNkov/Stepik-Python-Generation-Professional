from collections import defaultdict

data = defaultdict(int)
data['key'].append(1)
data['key'].append(2)
data['key'].append(3)

print(data['key'])


