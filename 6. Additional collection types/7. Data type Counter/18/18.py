from collections import Counter


with open('pythonzen.txt', encoding='utf-8') as file:
    data = file.read()

filtered_letters = filter(str.isalpha, data.lower())

counter = Counter(sorted(filtered_letters))
for letter, count in counter.items():
    print(f'{letter}: {count}')