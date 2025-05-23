import pickle


def filter_dump(filename, objects, typename):
    filtered_data = [obj for obj in objects if type(obj) == typename]
    with open(filename, 'wb') as file:
        pickle.dump(filtered_data, file)