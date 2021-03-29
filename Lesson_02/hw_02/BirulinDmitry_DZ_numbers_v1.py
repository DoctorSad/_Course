"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)
    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""

number = input('Введите число: ')
sum_ = 0
sequence = []

try:
    number = int(number)
except ValueError:
    exit('Число не введено')
except Exception as e:
    print('Программа завершает свою работу из-за ошибки (', e.__class__.__name__, "-->", e, ')')
    exit()

if not 1 <= number <= 999:
    print('Число не входит в диапазон')
elif len(str(number)) == 1:
    print('\nСумма цифр равна: ', number)
    print('При одной цифре порядок невозможно определить')
else:
    qty_of_digits = len(str(number))
    number_str = str(number)
    for i in number_str:
        sum_ += int(i)
        sequence.append(int(i))
    print('\nСумма цифр в введенном числе составляет: ', sum_)
    up = ''.join(sorted(number_str))
    down = ''.join(reversed(sorted(number_str)))
    if len(sequence) != len(set(sequence)):
        print('Цифры в числе введены вразброс')
    elif number == int(up):
        print('Цифры в числе введены по возрастанию')
    elif number == int(down):
        print('Цифры в числе введены по убыванию')

