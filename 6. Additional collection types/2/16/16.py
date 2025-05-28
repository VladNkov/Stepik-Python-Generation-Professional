intab = 'abcdefghijklmnopqrstuvwxyz'

outtab = input()
transtab = str.maketrans(intab, outtab)
input_answer = input().lower()
print(input_answer.translate(transtab))

