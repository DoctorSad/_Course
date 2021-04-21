"""
    Особенности описания чисел в коде.
"""

# Объявить читаемое длинное число можно использовав _ как разделитель
big_number = 42_123_333_123
print(big_number)  # 42123333123

# float числа являются не точными и при операции иногда встречаются погрешности
print(0.1 + 0.2)  # 0.30000000000000004

# так же оперировать float числами без целой части можно так (не рекомендуется)
print(.1 + .2)  # 0.30000000000000004

# для описания очень маленьких или очень больших чисел можно использовать e
print(15e-05)  # 0.00015
print(12e5)  # 1200000.0

"""
    Встроенные функции python для работы с числами
"""

# abs() - получить значение числа по модулю
print(abs(-123))  # 123

# round(num, ndigits) - округлить число num до ndigits знаков после запятой
# !!! Стоит обратить внимание, что round округляет "банковским" методом
print(round(3.1415, 2))  # 3.14

# pow(base, exp, mod) - возведение числа base в степень exp, аналог base ** exp
# передав необязательного аргумента mod - результат разделится по модулю на mod
print(pow(3, 10))  # 59049
print(3 ** 10)  # 59049

print(pow(3, 24, 2))  # 1
print(3 ** 24 % 2)  # 1

# min()/max() - возвращает минимальное/максимальное значение
print(min(14.23, -3.14, 123, -17))  # -17
print(max(14.23, -3.14, 123, -17))  # 123

# sum() - возвращает сумму переданной последовательности
a = 10
b = 20
c = 30

# необходимо передавать либо кортеж () либо список []
print(sum((a, b, c)))  # 60
print(sum([a, b, c]))  # 60

# divmod(x, y) - возвращает частное и остаток от деления x на y в виде кортежа
print(divmod(17, 5))  # (3, 2)  # 3 - частное, 2 - остаток от деления
print(17 // 5)  # 3
print(17 % 5)  # 2
