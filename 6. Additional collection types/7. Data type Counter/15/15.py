from collections import Counter


def count_occurences(word, words):
    word_list = words.lower().split(' ')
    count = Counter(word_list)
    return count[word.lower()]


word = 'Se'
words = 'se sdsf sds SE sdfsdg Se dhgf gfd asd se'

print(count_occurences(word, words))
