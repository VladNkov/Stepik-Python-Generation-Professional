from collections import Counter

data = input().split(',')
max_len = max(map(len, data))
# print(max_len)
for item, quantity in sorted(Counter(data).items()):

    price = sum(map(ord, item.replace(' ', '')))

    print(f'{item: <{max_len}}: {price} UC x {quantity} = {price*quantity} UC')