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
        pass


def sortbyvalue(to_sort):
    return to_sort[3]


def check(box, shattles):
    for shattle in shattles:
        print('Checking Shattle {}'.format(shattle))
        if len(shattle) > 0:
            toexit = 0
            for l_box in shattle:
                print('Checking box {}'.format(l_box))
                if box[0] in l_box[2] or l_box[0] in box[2]:
                    print('Суда низя')
                    toexit = 1
                    break
                else:
                    continue
            if toexit:
                print('Stop')
                continue
            else:
                print('Next')
                print('Добавляю1 {} в {}'.format(box, shattle))
                shattle.append(box)
                break
        else:
            print('Добавляю2 {} в {}'.format(box, shattle))
            shattle.append(box)
            break
    print('Here i am')

    return True

all = []
all_id = []
shattles = ([], [])

with open('test3.txt') as f:
    lst = f.read().split('\n')
    for i in lst:
        new_lst = i.split(';')
        new_lst[2] = new_lst[2].split(',')
        # all_id.append(new_lst[0])
        all.append(new_lst)

    all.sort(key=sortbyvalue, reverse=True)
    for i in all:
        print('Checking {} in {}'.format(i, shattles))
        check(i, shattles)
    print(shattles[0])
    print(shattles)
    print(all)


