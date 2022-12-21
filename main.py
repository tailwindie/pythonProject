'''
## №1
## Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def summ(num):

    if (',' in num):
        num = num.replace(',', '')

    num = num.replace('.', '')

    strlist = list(num)
    numsum = 0

    for i in strlist:
        i = int(i)
        numsum +=i

    print(f'Сумма цифр вашего числа = {numsum}')

num = input('Введите число больше 0: ')
summ(num)
'''
'''
## №2
## Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def multiplying(num):

    num = int(num)

    arr = [i*1 for i in range(1, num+1)]

    sumnum = 1
    arrNum = []
    for j in arr:
        sumnum *=j
        arrNum.append(sumnum)

    print(f'Набор произвдений от 1 до {num} = {arrNum} ')



num = input('Введите целое число: ')


if int(num)<1:
    print('Число должно быть больше 1!')
else:
    multiplying(num)
'''
'''
## №3
## Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

def sequence(num):

    arr = [i * 1 for i in range(1, num + 1)]
    sumnum = 0

    for j in arr:
        expr = (1+1/j)**j
        sumnum += expr

    return round(sumnum, 3)

num = int(input('Введите число: '))

print(sequence(num))
'''
'''
## №4
## Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

num = int(input("Ведите число: ")) # в данном случае >5, либо строку 85, 86 под замену
arr = []
for i in range(num):
    arr.append(random.randint(-num, num))
print(f'Ваш список: {arr}')

path = 'file.txt'
data = open(path, 'w')
data.write('2\n')
data.write('4\n')
data.close()

path = 'file.txt'
data = open(path, 'r')
multiply = 1
for line in data:
    multiply *= arr[int(line)]
print(multiply)
'''
'''
## №5
## Реализуйте алгоритм перемешивания списка.

import random

def shuffling(_list: list):
    shuffled_list = []
    temp_list = _list

    for _ in range(len(_list)):
        position = random.randint(0, len(temp_list) - 1)
        shuffled_list.append(temp_list.pop(position))
    return shuffled_list


print(shuffling([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
'''