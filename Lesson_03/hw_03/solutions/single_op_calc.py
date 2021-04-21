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

# 1. Решение без обработки ошибочного ввода и деления на 0
while True:
    n = int(input("Введите сколько чисел будет: "))
    op = input("Выберите операцию (+, -, *, /): ")

    result = int(input("Введите число: "))
    for _ in range(n - 1):
        if op == "+":
            result += int(input("Введите число: "))
        elif op == "-":
            result -= int(input("Введите число: "))
        elif op == "*":
            result *= int(input("Введите число: "))
        elif op == "/":
            result /= int(input("Введите число: "))
        else:
            print("Неверная операция. Попробуй еще раз")
            break
    else:
        print(result)
        if input("Continue? (Y/n) ") == "n":
            print("Bye!")
            break


# 2 есть обработка деления на 0, но без обработки ошибчного ввода
while True:
    n = int(input("Введіть кількість чисел : "))
    operation = input("Виберіть операцію: +, -, *, /: ")
    if operation == "+":
        result = 0
        i = 1
        while i <= n:
            number = int(input("Введіть число: "))
            result += number
            i += 1
        print(result)

    elif operation == "-":
        number = int(input("Введіть число: "))
        result = number
        i = 2
        while i <= n:
            number = int(input("Введіть число: "))
            result -= number
            i += 1
        print(result)

    elif operation == "*":
        result = 1
        i = 1
        while i <= n:
            number = int(input("Введіть число: "))
            result *= number
            i += 1
        print(result)

    elif operation == "/":
        number = int(input("Введіть число: "))
        result = number
        i = 1
        while i < n:
            number = int(input("Введіть число: "))
            try:
                result /= number
                i += 1
            except ZeroDivisionError:
                print("Ділення на 0 неможливе")
        print(result)

    else:
        print("Введені дані не коректні")

    if input("Continue? (Y/n) ") == "n":
        print("Bye!")
        break
