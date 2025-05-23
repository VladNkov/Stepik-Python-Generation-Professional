import pickle

filename = input().strip()
input_checksum = int(input().strip())
checksum = 0

with open(filename, 'rb') as file:
    obj = pickle.load(file)

if isinstance(obj, dict):
    checksum = sum(k for k in obj.keys() if isinstance(k, int))
elif isinstance(obj, list):
    int_el = [x for x in obj if isinstance(x, int)]
    if int_el:
        checksum = min(int_el) * max(int_el)
    else:
        checksum = 0

if checksum == input_checksum:
    print('Контрольные суммы совпадают')
else:
    print('Контрольные суммы не совпадают')
