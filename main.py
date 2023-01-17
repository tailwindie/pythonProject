'''
## №38
## Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

firstStr = 'Михаил абв Калугин аБВ хотел написать АбВ код. Получилось как всегда. АБВ'

secondStr = list(filter(lambda el: 'абв' not in el.lower(), firstStr.split() ))

print(f'Изначальная строка: ')
print(firstStr)
print(f'Строка без слов, содержащих "АБВ": ')
print(*secondStr)
'''
'''
## №2
## Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')

def getToss():

    toss = random.randint(1, 2)
    print(f'Подбрасываем монетку...')
    print(f'Ух ты, чуть на ребро не встала! Что же там выпало..?')

    if toss == 1:
        print(f'Решка! Первым ходит {player1}.')
        return (toss)
    elif toss == 2:
        print(f'Орёл! Первым ходит {player2}.')
        return (toss)

def turns(gotToss):

    startPoints = int(input('Введите стартовое количество конфет: '))
    maxPointsPR = int(input('Введите максимальное количество конфет, которое можно взять за ход: '))

    arrPlayer1 = []
    arrPlayer2 = []

    while startPoints >= 0:

        if gotToss == 1:

            tookPoints = int(input(f'{player1}, выберите количество конфет (от 1 до {maxPointsPR}): '))

            while (tookPoints > 28) or (startPoints - tookPoints < 0):
                print(f'Что-то не так... Либо конфет осталось меньше, чем вы хотите взять, либо вы выбрали число не от 1 до {maxPointsPR}.')
                tookPoints = int(input(f'{player1}, выберите количество конфет (от 1 до {maxPointsPR}): '))

            startPoints -= tookPoints

            print(f'{player1} взял {tookPoints} конфет. Всего осталось: {startPoints} \n')

            arrPlayer1.append(tookPoints)

            if startPoints > 0:
                gotToss = 2

            elif startPoints == 0:
                print(f'{player1} победил!')
                break

        if gotToss == 2:

            tookPoints = int(input(f'{player2}, выберите количество конфет (от 1 до {maxPointsPR}): '))

            while (tookPoints > 28) or (startPoints - tookPoints < 0):
                print(f'Что-то не так... Либо конфет осталось меньше, чем вы хотите взять, либо вы выбрали число не от 1 до {maxPointsPR}.')
                tookPoints = int(input(f'{player2}, выберите количество конфет (от 1 до {maxPointsPR}): '))

            startPoints -= tookPoints

            print(f'{player2} взял {tookPoints} конфет. Всего осталось: {startPoints} \n')

            arrPlayer2.append(tookPoints)

            if startPoints > 0:
                gotToss = 1

            elif startPoints == 0:
                print(f'{player2} победил!')
                break


gotToss = getToss()

turns(int(gotToss))
'''
'''
## №40
## Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(rawstring):

    encoded = ''
    prev_char = ''
    count = 1

    if not rawstring:
        return ''

    for char in rawstring:
        if char != prev_char:
            if prev_char:
                encoded += str(count) + prev_char

            count = 1
            prev_char = char

        else:
            count += 1

    else:
        encoded += str(count) + prev_char

    return encoded

def rle_decode(encodedstring):

    decode = ''
    count = ''

    for char in encodedstring:
        if char.isdigit():
            count += char

        else:
            decode += char * int(count)
            count = ''

    return decode

def main():

    print('Изначальная строка данных:')
    rawtext = 'AAAAAAAAAAAAAAABBBBBBBBBBBBBCCCCCCCCDDDDDDDDDDDD'
    print(rawtext)
    print()

    print('Сжатая строка данных:')
    compressed_text = rle_encode(rawtext)
    print(compressed_text)
    print()

    print('Распакованная строка:')
    decompressed_text = rle_decode(compressed_text)
    print(decompressed_text)

if __name__ == '__main__':
    main()
'''