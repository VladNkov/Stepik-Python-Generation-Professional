from collections import Counter

data = input().split(',')
for product, quantity in sorted(Counter(data).items()):
    print(f'{product}: {quantity}')