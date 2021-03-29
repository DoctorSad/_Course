"""
    Магическое число.
    Необходимо угадать загаданное число за наименьшее количество попыток.
    Алгоритм:
    1. Генерируется случайное число.
    2. Пользователь вводит число.
    3. Если введенное число больше или меньше сгенерированного, то
        выводится соответствующее сообщение и возвращаемся к пункту 2.
    4. Иначе введенное число равняется сгенерированному -
        пользователь угадал число. Выводится само число и количество попыток.
        А так же вопрос "Continue? (Y/n) ".
    6. Если пользователь выбирает продолжить -
        обнуляем счетчик попыток и переходим к пункту 1.
    7. Иначе выводим сообщение 'Bye!'.
    * Для генерации случайного числа используем random.randint(-inf, +inf),
        где -inf - +inf - диапазон возможных чисел
    ** по желанию, можете хранить рекордное число попыток
    и сообщать пользователю, если он поставил новый рекорд
"""

import random
count = 1
guess = None
record = 1000000

while True:
    for _ in range(20):
        print('\n')
    print('                  *** Магическое число ***')
    print('Введите нижний диапазон: ', end='')
    min_ = input()
    print('Введите верхний диапазон: ', end='')
    max_ = input()
    try:
        min_ = int(min_)
        max_ = int(max_)
    except ValueError:
        print('Вы не ввели диапазоны с типом <int>')
    else:
        magic_number = random.randint(min_, max_)
        while not guess:
            print('Введите число: ', end='')
            try:
                number = int(input())
            except ValueError:
                print('Вы не ввели число типа <int>')
                break
            if number > magic_number:
                print('Вы ввели число которое больше рандомного')
                count += 1
            elif number < magic_number:
                print('Вы ввели число которое меньше рандомного')
                count += 1
            elif number == magic_number:
                for _ in range(20):
                    print('\n')
                print('Вы угадали рандомное число <', magic_number, '>. Использовано попыток: ', count)
                if count < record:
                    print('Вы установили новый рекорд!')
                    record = count
                guess = 1
    out = input('                                    Continue (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
            count = 1
            guess = 0
            continue
    elif out == 'n':
        print('Bye!')
        break
