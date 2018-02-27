# coding: utf-8

# Домашнее задание2:

# Normal
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4] Результат: [3, 5, 2]

from math import sqrt

lst = [2, -5, 8, 9, -25, 25, 4]
new_lst = []

for i in lst:
    if i > 0:
        total = sqrt(i)
        if total % 1 == 0:
            new_lst.append(int(total))
print(new_lst)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2]
lst2 = set(lst)
lst1 = []

for i in lst:
    if lst.count(i) == 1:
        lst1.append(i)
print(lst1)

# Hard
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# equation = 'y = -12x + 11111140.2121'
# x = 2.5
# вычислите и выведите y

import re

equation = 'y = -12x + 11111140.2121'
x = 2.5

k = float(re.findall(r'[^=]\d+', equation)[0])
b = float(re.split(r'\+.', equation)[-1])

y = k * x - b

print(y)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты,
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
# ...
# 12 13 14
# 9 10 11
# 6 7 8
# 4 5
# 2 3
# 1
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
# Выходные данные: Два целых числа — номер этажа и порядковый номер слева на этаже.
# Пример:
# Вход: 13
# Выход: 6 2
# Вход: 11
# Выход: 5 3

# Решение, которое было на уроке
#
# N = 1515
#
# floor = 1
# room = 1
#
# answer_floor = 0
# answer_room = None
#
# while N > 0:
#     for current_floor in range(floor):
#         answer_floor += 1
#         for current_room in range(room):
#             N -= 1
#             if N == 0:
#                 answer_room = current_room + 1
#                 break
#         if N == 0:
#             break
#     floor += 1
#     room += 1
# print(answer_floor, answer_room)

# Тот алгоритм, который был показан на занятии - я еле понял.
# С подачи коллеги на работе был выработан немного другой алгоритм, который, вроде как,
# тоже правильно работает. Он мне понянее и написал его я сам.

n = 15151515151515

square = 1
answer_floor = 0
answer_room = 0

while n > 0:
    n = n - (square ** 2)
    if n <= 0:
        room_square = (square ** 2) + n
        floor_min = (square - 1) * (square / 2)
        answer_floor = int(floor_min + room_square // square)
        answer_room = square
        if room_square % square != 0:
            answer_floor += 1
            answer_room = room_square % square
        break
    else:
        square += 1
print(answer_floor, answer_room)


# Домашнее задание №3:

# EASY
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
# def my_round(number, ndigits):
# pass
# my_round(2.1234567, 5)

# Было

def my_round(number, ndignits):
    my_number = list(str(number))
    point_position = my_number.index('.')
    left_part = my_number[:point_position + 1]
    left_part = ''.join(left_part)
    right_part = my_number[point_position + 1:]
    right_part = ''.join(right_part)
    right_part_end = int(right_part[ndignits])
    right_part_result = int(right_part[:ndignits])
    if right_part_end >= 5:
        right_part_result += 1
    result = float('{}{}'.format(left_part, right_part_result))
    print(result)
    print(type(result))


my_round(2.555555555555555555555555555555555, 10)

# Стало

import re


def my_round(number, ndignits):
    dignits = re.split(r'[\.]', str(number))
    total = int(str(dignits[-1])[:ndignits])
    if int(str(dignits[-1])[:ndignits]) >= 5:
        total += 1
    result = float(str('{}.{}'.format(dignits[0], total)))
    print(result)


my_round(2.1234567, 5)


# Получилось короче, чем в первый раз и немного другая логика

# NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
# def fibonacci(n, m):
# pass

# Было
def fibonacci(n, m):
    numbers = [1, 1]
    for element in range(m - 2):
        numbers.append(numbers[-1] + numbers[-2])
    print(numbers[n - 1:])


fibonacci(3, 15)


# Стало (переписывал не глядя, что писал в первый раз)
def fibonacci(n, m):
    fib = [1, 1]
    while len(fib) < m + 1:
        fib.append(fib[len(fib) - 2] + fib[len(fib) - 1])
    print(fib[n:])


fibonacci(1, 10)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
# def sort_to_max(origin_list):
# pass
# sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Было

def sort_to_max(origin_list):
    count = 1
    while count > 0:
        count = 0
        for step in range(len(origin_list) - 1):
            if origin_list[step] > origin_list[step + 1]:
                tmp = origin_list[step + 1]
                if origin_list.count(tmp) > 1:
                    origin_list.insert(step, tmp)
                    tmp_ind = origin_list.index(tmp, step + 1)  # Вот тут были сложности. Индекс в итоге подобрал.
                    origin_list.pop(tmp_ind)
                else:
                    origin_list.remove(origin_list[step + 1])
                    origin_list.insert(step, tmp)
                count += 1
    print(origin_list)


sort_to_max([2, 10, 200, -12, 2.5, 20, -11, 4, 4, 0])


# Стало

def sort_to_max(origin_list):
    count = 1
    while count > 0:
        count = 0
        for element in range(len(origin_list) - 1):
            if origin_list[element] > origin_list[element + 1]:
                origin_list.insert(element, origin_list[element + 1])
                origin_list.pop(element + 2)
                count += 1
    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

# насколько я понял принцип работы функции filter

mixed = ['мак', 'просо', 'мак', 'мак', 'просо', 'мак', 'просо', 'просо', 'просо', 'мак']


def filt(example, source):
    return (i for i in mixed if i == 'мак')


result = list(filt('мак', mixed))
print(result)

# Задание-2: Файлы для задания ищи в материалах
# Дана ведомость расчета заработной платы (файл "workers.txt").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "hours_of.txt"

# Не понимаю, почему вывод идёт не равномерный. Смещение вправо после фамилии "Алексеев"

import os
import re

path = os.path.join('files', 'workers.txt')
path_hours = os.path.join('files', 'hours_of.txt')
path_results = os.path.join('files', 'results.txt')

with open(path_results, 'w', encoding='UTF-8') as r:
    r.write('Фамилия' + '\t' + '\t' + 'Имя' + '\t' + '\t' + '\t' + 'Заработал' + '\n')
    r.close()
    with open(path, 'r', encoding='UTF-8') as f:
        for s in f:
            if 'Норма_часов' not in s:
                worker = re.split(r'\W+', s)[:5]
                with open(path_hours, 'r', encoding='UTF-8') as h:
                    for line in h:
                        hours = re.split(r'\W+', line)[:3]
                        # начало вычислений
                        if worker[0] == hours[0] and worker[1] == hours[1]:
                            print('{} {}'.format(worker, hours))
                            with open(path_results, 'a', encoding='UTF-8') as r:
                                if int(hours[2]) >= int(worker[4]):
                                    payment = int(worker[2]) + ((int(worker[2]) / int(worker[4])) * 2) *
                                    int(hours[2]) - int(worker[4])
                                r.write(str(worker[0] + '\t' + '\t' + worker[1] + '\t' + '\t' + '\t' +
                                            str(float('{0:.7}'.format(payment))) + '\n'))
                                continue
                            else:
                            payment = (int(worker[2]) / int(worker[4])) * (int(hours[2]))
                            r.write(str(worker[0] + '\t' + '\t' + worker[1] + '\t' + '\t' + '\t' +
                                        str(float('{0:.7}'.format(payment))) + '\n'))
                            continue

# Задание-3: Файл для задания ищи в материалах
# Дан файл ("fruits.txt") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))


import os

path = os.path.join('files', 'fruits.txt')
path_new = os.path.join('files', 'result', '')

with open(path, 'r', encoding='UTF-8') as f:
    for i in f:
        if i[0] in list(map(chr, range(ord('А'), ord('Я') + 1))):
            with open(path_new + 'fruit_' + i[0] + '.txt', 'a', encoding='UTF-8') as new:
                new.write(i)

# Домашнее задание №4:

# NORMAL
import re

# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO' \
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK' \
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn' \
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa' \
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete' \
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ' \
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb' \
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC' \
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB' \
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT' \
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu' \
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB' \
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa' \
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ' \
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# Способ-2 (первый и так понятен)

# Было

pattern = list(map(chr, range(ord('A'), ord('Z') + 1)))
lower = []
for el in line:
    if el not in pattern:
        lower.append(el)
    else:
        lower.append('.')
string_lower = ''
for i in lower:
    string_lower += i
lower = string_lower.split('.')
while lower.count('') > 0:
    lower.remove('')
print(lower)

# Стало

ruler = list(map(chr, range(ord('A'), ord('Z') + 1)))
lst = [i for i in line]
for i in lst:
    if i in ruler:
        lst[lst.index(i)] = '.'
temp_string = ''.join(lst)
new_lst = temp_string.split('.')
new_lst = [i for i in new_lst if i != '']
print(new_lst)

# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
# line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
# 'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
# 'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
# 'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
# 'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
# 'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
# 'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
# 'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
# 'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
# 'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
# 'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
# 'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
# 'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
# 'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
# 'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Способ c re
lst = re.findall('[a-z][a-z]([A-Z]+)[A-Z][A-Z]', line_2)
print(lst)

# Способ без re
lst = [i for i in line_2]
new_lst = []

low = 0
upp = 0
flag = 0

for i in lst:
    if i.islower():
        low += 1
        flag = 0
        if 2 > upp > 0:
            flag = 0
            upp = 0
            new_lst.pop(len(new_lst) - 1)
        elif upp >= 2:
            for num in range(2):
                new_lst.pop(len(new_lst) - 1)
            upp = 0
            new_lst.append('.')
    if i.isupper():
        if flag == 0:
            if low >= 2:
                flag = 1
                low = 0
            else:
                low = 0
        if flag == 1:
            upp += 1
            new_lst.append(i)
new_str = ''.join(new_lst)
new_lst = new_str.split('.')
for item in new_lst:
    if item == '':
        new_lst.remove(item)
print(new_lst)

# Задание-3:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
import os
from random import randint

last = 0
max_digit = 0
cur_count = 0
max_count = 0

with open('text.txt', 'w', encoding='UTF-8') as f:
    for i in range(2500):
        rand = randint(0, 9)
        f.write(str(rand))
with open('text.txt', 'r', encoding='UTF-8') as f:
    digits = f.read()
    for dig in digits:
        if dig != last:
            if cur_count > max_count:
                max_count = cur_count
                max_digit = last
            last = dig
            cur_count = 1
        else:
            cur_count += 1
print(digits)
print('{} цифр {} подряд'.format(max_count, max_digit))

# HARD

# Задание-2:
# Найдите наибольшее произведение пяти последовательных цифр в 1000-значном числе.
# Выведите произведение и индекс смещения первого числа последовательных 5-ти цифр.
# Пример 1000-значного числа:
# number = """
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450"""
from random import randint

max_mult = 0
dig_mult = 0
dig_index = 0

string = ''.join([str(i) for i in range(1000)])
print(string)

for i in range(len(string)):
    if len(string) - i > 5:
        dig_mult = int(string[i]) * int(string[i + 1]) * int(string[i + 2]) * int(string[i + 3]) * int(string[i + 4])
        if dig_mult > max_mult:
            max_mult = dig_mult
            dig_index = i
print('Наибольшее произведение - {}, из чисел {}'.format(max_mult, string[dig_index:dig_index + 5]))








