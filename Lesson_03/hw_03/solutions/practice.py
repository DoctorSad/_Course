"""
    Реализовать программу, с помощью которой можно (меню):
    1. Найти наибольшую цифру числа n.
    2. Найти количество четных и нечетных цифр в числе n.
    3. Узнать, является ли число n простым.
    4. Отобразить ряд простых чисел от 2 до n через запятую.
"""

while True:
    print(
        "1. Найти наибольшую цифру числа n.\n"
        "2. Найти количество четных и нечетных цифр в числе n.\n"
        "3. Узнать, является ли число n простым.\n"
        "4. Отобразить ряд простых чисел от 2 до n через запятую.\n"
        "5. Выход."
    )
    menu_item = input()

    if menu_item == "1":
        n = input("Введите число: ")
        try:
            n = int(n)
        except ValueError:
            print("Введено не число.")
        else:
            max_digit = 0
            while n > 0:
                digit = n % 10
                if digit > max_digit:
                    max_digit = digit
                n //= 10

            print("Наибольшая цифра:", max_digit)
            input("\nНажмите Enter для продожения\n")

    elif menu_item == "2":
        n = input("Введите число: ")
        try:
            n = int(n)
        except ValueError:
            print("Введено не число.")
        else:
            even = odd = 0
            while n > 0:
                digit = n % 10
                if digit % 2 == 0:
                    even += 1
                else:
                    odd += 1
                n //= 10

            print("Четных цифр:", even, ", нечетных:", odd)
            input("\nНажмите Enter для продожения\n")

    elif menu_item == "3":
        n = input("Введите число: ")
        try:
            n = int(n)
        except ValueError:
            print("Введено не число.")
        else:
            if n < 2:
                print("Число должно быть больше 1")
            elif n == 2:
                print(n, "- простое число")
            else:
                for i in range(2, n + 1):
                    if n % i == 0:
                        print(n, "- составное число")
                        break
                else:
                    print(n, "- простое число")

        input("\nНажмите Enter для продожения\n")

    elif menu_item == "4":
        n = input("Введите число: ")
        try:
            n = int(n)
        except ValueError:
            print("Введено не число.")
        else:
            if n < 2:
                print("Число должно быть больше 1")
            else:
                for a in range(2, n + 1):
                    for b in range(2, a + 1):
                        if a % b == 0:
                            if a == b:
                                print(a, end=", ")
                            break
                print()

        input("\nНажмите Enter для продожения\n")

    elif menu_item == "5":
        print("Пока!")
        break
