"""
    1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,
        если больше в верхнем - вывести все в верхнем,
        если поровну - вывести в противоположных регистрах.

    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

    3. Если длина строки больше 20, то обрезать лишние символы до 20.
        Иначе дополнить строку символами '@' до длины 20.
    (можно использовать метод ljust либо конкатенацию и дублирование (+ и *))

    После выполнения кажого пункта выводить результат типа:
        1. Исходная строка: "здесь_исходная_строка".
        Результат: "здесь_измененная_строка_после_выполненного_пункта".
    (Использовать форматирование строк f'{}')
"""

while True:
    for _ in range(20):
        print('\n')
    my_string = input('Введите строку: ')
    lower = 0
    upper = 0
    out = ''
    for i in my_string:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
    if lower > upper:
        out = my_string.lower()
    elif upper > lower:
        out = my_string.upper()
    elif upper == lower:
        for i in my_string:
            if i.islower():
                i = i.upper()
                out = out + i
                continue
            elif i.isupper():
                i = i.lower()
                out = out + i
                continue
            out = out + i
    for _ in range(20):
        print('\n')
    print('1. Если в строке больше символов в нижнем регистре - вывести все в нижнем,')
    print('если больше в верхнем - вывести все в верхнем,')
    print('если поровну - вывести в противоположных регистрах.')
    print(f'\nИсходная строка: "{my_string}".')
    print(f'Результат: "{out}".')
    print('\nИдем дальше?', end='')
    input()

    """ ----------------------------------------------------------------------------------- """

    out_str = []
    count = 0
    max_ = 0
    break_operation = 0
    out = ''
    for _ in range(20):
        print('\n')
    string_punctuation = ',. '
    temp_string = ''
    temp2_string = my_string + ' '
    for i in temp2_string:
        if string_punctuation.find(i) == -1:
           temp_string += i
           count = 0
        elif bool(string_punctuation.count(i)) and count == 0:
            count += 1
            out_str.append(temp_string)
            temp_string = ''
    for i in out_str:
        if not i[0].isupper():
            break_operation = 1
            break
    if break_operation == 1:
        out = 'draft: ' + temp2_string[5:]
    elif break_operation != 1:
        out = 'done. ' + temp2_string
    print('2. Если в строке каждое слово начинается с заглавной буквы, тогда')
    print('добавить в начало строки "done. ".')
    print('Иначе заменить первые 5 элементов строки на "draft: ".')
    print(f'\nИсходная строка: "{my_string}".')
    print(f'Результат: "{out}".')
    print('\nИдем дальше?', end='')
    input()

    """ ----------------------------------------------------------------------------------- """

    out = ''
    end_program = None
    for _ in range(20):
        print('\n')
    if len(my_string) > 20:
        out = my_string[:20]
    else:
        out = my_string + '@' * (20 - len(my_string))
    print('3. Если длина строки больше 20, то обрезать лишние символы до 20.')
    print('Иначе дополнить строку символами "@" до длины 20.')
    print(f'\nИсходная строка: "{my_string}".')
    print(f'Результат: "{out}".')
    end_program = input('                                    Будем вводить новую строку (Y/n)?: ')
    if not end_program or end_program == 'Y':
        for _ in range(20):
            print('\n')
        my_string = None
        lower = 0
        upper = 0
        out = ''
        out_str = []
        count = 0
        max_ = 0
        break_operation = 0
        continue
    elif end_program == 'n':
        break
