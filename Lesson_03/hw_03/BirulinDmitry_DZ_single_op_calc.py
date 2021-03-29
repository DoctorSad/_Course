"""
    Программа считает сумму/разницу/произведение/частное n чисел.
    Алгоритм:
    1. Пользователь вводит число n.
    2. Затем выбирает операцию (+, -, *, /).
    3. После этого вводит n чисел.
    4. Программа выводит результат и сообщение "Continue? (y/n)".
    5. Если пользователь вводит y, то программа выполняется сначала.
        Иначе - выводит сообщение 'Bye!' и прекращает свою работу.
"""
list_of_numbers = []
result = None

while True:
    for _ in range(20):
        print('\n')
    print('                  *** Программа считает сумму/разницу/произведение/частное n чисел ***')
    qty_of_numbers = input('\nВведите количество чисел: ')
    try:
        qty_of_numbers = int(qty_of_numbers)
    except ValueError:
        exit('Не введено количество чисел в виде числа')
    operation = input('Введите операцию (+, -, *, /): ')
    q = 0
    while q < qty_of_numbers:
        print('Введите <', q + 1, '>' ' число: ', end='')
        a = input()
        try:
            a = int(a)
        except ValueError:
            exit('Не введено число')
        list_of_numbers.append(a)
        q += 1

    i = 0
    for y in list_of_numbers:
        if operation == '+':
            if i == 0:
                result = list_of_numbers[0]
                i += 1
                continue
            result += y
        elif operation == '-':
            if i == 0:
                result = list_of_numbers[0]
                i += 1
                continue
            result -= y
        elif operation == '*':
            if i == 0:
                i += 1
                result = list_of_numbers[0]
                continue
            result *= y
        elif operation == '/':
            if i == 0:
                i += 1
                result = float(list_of_numbers[0])
                continue
            try:
                result /= float(y)
            except ZeroDivisionError:
                exit('Деление на ноль!')

    print('Результат операции равен: ', result)
    out = input('                                    Continue (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
            result = None
            list_of_numbers.clear()
        continue
    elif out == 'n':
        print('Bye!')
        break
