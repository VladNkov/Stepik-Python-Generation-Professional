from collections import defaultdict

def best_sender(messages, senders):
    d_dict = defaultdict(int)
    for key, value in zip(senders, messages):
        d_dict[key] += len(value.split(' '))

    return max(sorted(d_dict, reverse=True), key=d_dict.get)


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))
messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))