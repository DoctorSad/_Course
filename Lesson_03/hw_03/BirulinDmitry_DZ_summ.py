"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.
    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение нечетных чисел числового ряда.
    * обработать возможные ошибки
    ----------------------------------------
"""

list_of_numbers = []
result_plus = 0
result_umnojenie = 1

while True:
    print('Начало ряда: ', end='')
    begin = input()
    if begin == '':
        begin = 0
    begin = int(begin)
    print('Конец ряда: ', end='')
    end = int(input())

    if begin >= end:
        print('Нет числового ряда')
    else:
        for i in range(begin, end + 1):
            result_plus += i

        if not begin % 2:
            begin = begin + 1

        for i in range(begin, end + 1, 2):
            result_umnojenie *= i

        print('Сумма числового ряда равна: ', result_plus)
        print('Произведение нечетных чисел числового ряда равно: ', result_umnojenie)
    out = input('                                    Continue (Y/n)?: ')

    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
            result_plus = 0
            result_umnojenie = 1
        continue
    elif out == 'n':
        print('Bye!')
        break
