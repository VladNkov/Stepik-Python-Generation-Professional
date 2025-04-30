import sys

temp = sys.stdin.read().split('\n')
# print(temp)
for t in temp:
    print(t[::-1])