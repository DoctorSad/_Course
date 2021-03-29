"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)
    1. Найти сумму цифр числа.
    2. Вывести на экран, порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""

number = input('Введите число: ')
poryadok = input('Введите порядок вывода цифр (возрастание - 1, убывание - 2): ')
sum_ = 0
number_for_exit = None

try:
    number = int(number)
except ValueError:
    exit('Число не введено')
except Exception as e:
    print('Программа завершает свою работу из-за ошибки (', e.__class__.__name__, "-->", e, ')')
    exit()

try:
    poryadok = int(poryadok)
except ValueError:
    exit('Порядок вывода должен равняться либо 1 либо 2')
except Exception as e:
    print('Программа завершает свою работу из-за ошибки (', e.__class__.__name__, "-->", e, ')')
    exit()

if poryadok != 1 and poryadok != 2:
    exit('Порядок вывода должен равняться либо 1 либо 2')

if not 1 <= number <= 999:
    print('Число не входит в диапазон')
else:
    qty_of_digits = len(str(number))
    number_str = str(number)
    for i in number_str:
        sum_ += int(i)
    print('\nСумма цифр в введенном числе составляет: ', sum_)
    number_for_exit = sorted(number_str)
    if qty_of_digits > 1:
        if poryadok == 1:
            number_for_exit = ''.join(number_for_exit)
            print('Порядок чисел по возрастанию: ', number_for_exit)
        else:
            number_for_exit = ''.join(reversed(number_for_exit))
            print('Порядок чисел по убыванию: ', number_for_exit)
    else:
        print('Порядок чисел не имеет значения (число из одной цифры): ', sum_)



