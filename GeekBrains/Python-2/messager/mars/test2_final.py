import sys

"""
Я только учусь, поэтому очень хотел бы получить небольшое кодревью (понимаю, что сквозь кровь из глаз, но всё же)
и пример того, как надо было решить эту и предыдущую задачу.
Спасибо!
"""


def sortbyvalue(to_sort):
    return int(to_sort[3]) / int(to_sort[1])


def check(box, shuttles):
    for shuttle in shuttles:
        if len(shuttle) > 0:
            toexit = 0
            total_weight = 0
            for l_box in shuttle:
                total_weight += int(l_box[1])
            if total_weight + int(box[1]) <= 200:
                for l_box in shuttle:
                    if box[0] in l_box[2] or l_box[0] in box[2]:
                        toexit = 1
                        break
                    else:
                        continue
                if toexit:
                    continue
                else:
                    shuttle.append(box)
                    all.remove(box)
                    break
            else:
                continue
        else:
            shuttle.append(box)
            all.remove(box)
            break


def print_shuttle(shuttle):
    total_boxes = ''
    for i in shuttle:
        total_boxes += i[0] + ';'
    print(total_boxes)


all = []
shuttles = ([], [])

while True:
    try:
        line = sys.stdin.readline().split('\n')
    except KeyboardInterrupt:
        break
    if not line:
        break
    if len(line[0]) < 1:
        break

    new_lst = line[0].split(';')
    new_lst[2] = new_lst[2].split(',')
    all.append(new_lst)

all.sort(key=sortbyvalue, reverse=True)
for i in all:
    check(i, shuttles)
for shuttle in shuttles:
    print_shuttle(shuttle)
