import sys

# ID;Вес;ID несовместимых предметов через запятую;Ценность для экспедиции;

def sortbyvalue(to_sort):
    return int(to_sort[3]) / int(to_sort[1])


def check(box, shuttles):
    for shuttle in shuttles:
        # print('Checking shuttle {}'.format(shuttle))
        if len(shuttle) > 0:
            toexit = 0
            total_weight = 0
            for l_box in shuttle:
                total_weight += int(l_box[1])
            # print('Total WEIGHT = {}, next box += {}'.format(total_weight, int(box[1])))
            if total_weight + int(box[1]) <= 200:
                for l_box in shuttle:
                    # print('Checking box {}'.format(l_box))
                    if box[0] in l_box[2] or l_box[0] in box[2]:
                        # print('Суда низя')
                        toexit = 1
                        break
                    else:
                        continue
                if toexit:
                    # print('Stop')
                    continue
                else:
                    # print('Next')
                    # print('Добавляю1 {} в {}'.format(box, shuttle))
                    shuttle.append(box)
                    all.remove(box)
                    break
            else:
                continue
        else:
            # print('Добавляю2 {} в {}'.format(box, shuttle))
            shuttle.append(box)
            all.remove(box)
            break
    # print('Here i am')


def print_shuttle(shuttle):
    total_boxes = ''
    for i in shuttle:
        total_boxes += i[0] + ';'
    print(total_boxes)


all = []
shuttles = ([], [])


with open('test2.txt') as f:
    lst = f.read().split('\n')
    for i in lst:
        new_lst = i.split(';')
        new_lst[2] = new_lst[2].split(',')
        # all_id.append(new_lst[0])
        all.append(new_lst)

    all.sort(key=sortbyvalue, reverse=True)
    for i in all:
        # print('Checking {} in {}'.format(i, shuttles))
        check(i, shuttles)
    # print(shuttles[0])
    # print(shuttles)
    print(all)
    for shuttle in shuttles:
        print_shuttle(shuttle)
