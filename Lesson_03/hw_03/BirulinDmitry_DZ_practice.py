"""
    Реализовать программу, с помощью которой можно (меню):
    1. Найти наибольшую цифру числа n.
    2. Найти количество четных и нечетных цифр в числе n.
    3. Узнать, является ли число n простым.
    4. Отобразить ряд простых чисел от 2 до n через запятую.
"""

while True:
    for _ in range(20):
        print('\n')
    print('Введите число:')
    number = input('')
    max_digit = 0
    parnie_digit = 0
    neparnie_digit = 0
    prostiye_4isla = []
    try:
        number = int(number)
    except ValueError:
        print('Не введено число!')
    else:

        # 1. Найти наибольшую цифру числа n.
        for i in str(number):
            if int(i) > max_digit:
                max_digit = int(i)
        print(f'\nНаибольшая цифра числа: {max_digit}')
        input()

        # 2. Найти количество четных и нечетных цифр в числе n.
        for i in str(number):
            if int(i) % 2:
                neparnie_digit += 1
            elif not int(i) % 2:
                parnie_digit += 1
        print(f'Четных цифр: {parnie_digit}')
        print(f'Нечетных цифр: {neparnie_digit}')
        input()

        # 3. Узнать, является ли число n простым.
        if number < 2:
            print('Введенное число не может быть простым (меньше двух)')
        else:
            simple = 0
            delitel = 2
            while delitel < number:
                if not number % delitel:
                    simple += 1
                    if simple:
                        break
                delitel += 1
            if simple:
                print('Число не является простым')
            else:
                print('Число простое')
            input()

        # 4. Отобразить ряд простых чисел от 2 до n через запятую.
        if number < 2:
            print('Введенное число не может быть простым (меньше двух)')
        else:
            perebor = number
            while perebor >= 2:
                simple = 0
                delitel = 2
                while delitel < perebor:
                    if not perebor % delitel:
                        simple += 1
                    delitel += 1
                if not simple:
                    prostiye_4isla.append(perebor)
                perebor -= 1
                simple = 0
            index = 0
            prostiye_4isla.reverse()
            print('Список простых чисел: ')
            vivod = 0
            for q in prostiye_4isla:
                if vivod == 10:
                    vivod = 0
                    print('\n', end = '')
                if not index + 1 == len(prostiye_4isla):
                    print(f'{q}, ', end='')
                else:
                    print(f'{q}', end='')
                index += 1
                vivod +=1
    print('\n')
    end_program = input('                                    Новое число (Y/n)?: ')
    if not end_program or end_program == 'Y':
        continue
    elif end_program == 'n':
        break