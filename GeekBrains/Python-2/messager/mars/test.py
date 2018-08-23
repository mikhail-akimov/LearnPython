# import re
# import hashlib
#
#
# with open('test3.txt') as f:
#     string = f.read()
#     lst = re.findall('{.*?}', string)
#     start = 1
#     string = ''
#     while len(lst) > 0:
#         for i in lst:
#             if eval(i)['l'] == start:
#                 string = string + eval(i)['s']
#                 lst.remove(i)
#                 start += 1
#     print(string)
#
# print(hashlib.md5(string.encode('utf-8')).hexdigest())
#
#
# #One of the three ship's landers is malfunctioning. Two operate fully. The expedition team must load the most valuable equipment aboard the operating landers.\n\nHowever, some items of equipment are incompatible to be stored together and must be loaded into separate landers. Sufficient condition for incompatibility is incompatibility of the first object with the second, the second does not need to be incompatible with the first, but they cannot be loaded together anyway.\n\nThe file attached to this task contains a list of equipment in the following format: ID;Weight; Comma-Separated IDs of Incompatible Objects;Value Rating;\n\nUsing this data and knowing the landers maximum weight capacity (200 kg each), please write a program to select the most valuable equipment to load into the landers within the time limit and the compatibility restrictions...........


# ID;Вес;ID несовместимых предметов через запятую;Ценность для экспедиции;

class Item:
    def __init__(self, id, weight, errors, value):
        self.id = id
        self.weight = weight
        self.errors = errors
        self.value = value


class Module:
    def __init__(self):
        self.maxweight = 200
        self.on_board = []


    def __set__(self, instance, value):
        for i in Module.mro()

all = []
# ship1 = {}
# ship2 = {}
# empty = 1
# with open('test3.txt') as f:
#     lst = f.read().split('\n')
#     for i in lst:
#         new_lst = i.split(';')
#         new_lst[2] = new_lst[2].split(',')
#         all.append(new_lst)
#     while empty:


with open('test3.txt') as f:
    lst = f.read().split('\n')
    for i in lst:
        new_lst = i.split(';')
        new_lst[2] = new_lst[2].split(',')
        all.append(new_lst[0])
        new_lst[0] = Item(new_lst[0], new_lst[1], new_lst[2], new_lst[3])

