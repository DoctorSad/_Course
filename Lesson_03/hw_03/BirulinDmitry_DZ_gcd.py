"""
    Алгоритм Евклида. НОД - наибольший общий делитель
    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.
"""

while True:
    for _ in range(20):
        print('\n')
    print('     *** Алгоритм Евклида ***     ')
    num_1 = input('Введите первое число: ')
    num_2 = input('Введите второе число: ')
    tmp_1 = None
    tmp_2 = None

    try:
        tmp_1 = int(num_1)
        tmp_2 = int(num_2)
    except ValueError:
        print('Не введены два числа для вычислений')
    else:
        while True:
            if not tmp_1 or not tmp_2:
                nod = tmp_1 + tmp_2
                print('\nНаибольший общий делитель: ', nod)
                break
            elif tmp_1 == tmp_2:
                print('\nНаибольший общий делитель: ', tmp_1)
                break
            elif tmp_1 > tmp_2:
                tmp_1 %= tmp_2
            elif tmp_2 > tmp_1:
                tmp_2 = tmp_2 % tmp_1

    out = input('                                    Новая пара чисел (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
        continue
    elif out == 'n':
        break
