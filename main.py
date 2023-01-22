'''
## №30
## Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.

n = int(input(f'Введите количество элементов прогрессии: '))
nStart = int(input(f'Введите первый элемент прогрессии: '))
nStep = int(input(f'Введите разность элементов прогрессии: '))

def getProgression():

    arr = []
    for _ in range(n):
        arr.insert(i, (nStart + nStep * i))

    return arr

prog = getProgression()
print(prog)

'''
'''
## №31
## Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону

from random import randint

low = int(input('Введите минимальный порог для чисел: '))
high = int(input('Введите максимальный порог для чисел: '))

def getList():

    arr = [randint(-10, 10) for _ in range(10)]
    print(f'Изначальный массив: {arr} \n')

    return arr

def indexes(gotArr):

    inds = [i for i, v in enumerate(gotArr) if low <= v <= high]
    print(f'Индексы выбранных чисел: {inds} \n')


gotArr = getList()

indexes(gotArr)
'''
'''
## №32
## Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

num = int(input(f'Введите число: '))
exp = int(input(f'Введите степень: '))

def power(num,exp):

    if exp == 1:
        return num

    elif exp == 0:
        return 1

    elif exp != 1 and exp != 0:
        return (num * power(num, exp - 1))

print(f'Результат возведения числа {num} в {exp} степень: {power(num,exp)}')
'''