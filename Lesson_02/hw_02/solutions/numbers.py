"""
    Вводится число от 1 до 999
    (если введено не число либо число вне диапазона - вывести сообщение)

    1. Найти сумму цифр числа.
    2. Вывести на экран порядок, в котором расположены цифры числа
        (возростание/убывание/в разброс(равны))
"""

try:
    number = int(input("number: "))
except ValueError:
    print("You must enter a number.")
else:
    # if not 1 <= number <= 999:  # проверка, что число в нужном диапазоне
    if number < 1 or number > 999:  # проверка, что число в нужном диапазоне
        print("Number must be from 1 to 999.")
    else:
        first = number // 100  # получаем 1 цифру
        second = number // 10 % 10  # получаем 2 цифру
        third = number % 10  # получаем 3 цифру

        print("1.", first + second + third)  # выводим сумму цифр

        if first < second < third:
            result = "increasing"
        elif first > second > third or first == 0 and second > third:
            result = "decreasing"
        else:
            result = "one-digit number / random / equal"

        print("2.", result)

# так же можно разделить решение для чисел 1-9, 10-99 и 100-999
if 1 <= number <= 9:
    ...
elif 10 <= number <= 99:
    ...
elif number <= 999:
    number = 123
    a = 1
    b = 2
    c = 3

    if a < b < c:
        ...
    elif a > b > c:
        ...
    else:
        ...
else:
    print("Number must be from 1 to 999.")
