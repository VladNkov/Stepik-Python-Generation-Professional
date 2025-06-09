from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if by_values == False:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
        return ordered_dict

    else:
        for i in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(i)
        return ordered_dict


data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
print(data)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)
print(*data.items())
