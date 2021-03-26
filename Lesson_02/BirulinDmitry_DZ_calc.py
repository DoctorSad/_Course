"""
    Необходимо написать простой калькулятор,
    который оперирует с двумя числами и оператором.
    В зависимости от введенного оператора,
    между числами проводится определенная операция.
    Результат выводится на экран.
    * обработать все возможные ошибки программы с помощью try-except
"""

operation_text = None
res = None
num_1 = input("Введите число №1: ")
num_2 = input("Введите число №2: ")
operation = input("Какое действие вычисляем с числами (+, -, *, /)?: ")

try:
    num_1 = float(num_1)
    num_2 = float(num_2)
    if operation == '/':
        res = num_1 / num_2
except ValueError:
    exit('Не введены два числа для вычислений')
except ZeroDivisionError:
    exit('На ноль делить нельзя')
except Exception as e:
    print('Программа завершает свою работу из-за ошибки (', e.__class__.__name__, "-->", e, ')')
    exit()

if operation != '+' and operation != '-' and operation != '*' and operation != '/':
    exit('Некорректно введенная операция калькулятора')
elif operation == '+':
    res = num_1 + num_2
    operation_text = 'сложения'
elif operation == '-':
    res = num_1 - num_2
    operation_text = 'вычитания'
elif operation == '*':
    res = num_1 * num_2
    operation_text = 'умножения'
else:
    res = num_1 / num_2
    operation_text = 'деления'

print('Результат выполнения операции', operation_text, 'между числами', num_1, 'и', num_2, ': ')
print(round(res, 4))
