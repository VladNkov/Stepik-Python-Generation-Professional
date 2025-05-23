import pickle, sys

input_data = sys.stdin.read().splitlines()
pickle_file, argument = input_data[0], input_data[1:]

with open(pickle_file, 'rb') as file:
    pickle_func = pickle.load(file)

result = pickle_func(*argument)
print(result)
