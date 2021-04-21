"""
    При запуске программы выбор:
    1. Найти количество четных и нечетных цифр числа.
    2. Найти факториал числа.
    3. Сумма чисел.
    4. Выход.

    * после выполнения пунктов 1-3 попадаем обратно в меню.
"""
import random

while True:
    print(
        "1. Найти количество четных и нечетных цифр числа.",
        "2. Найти факториал числа.",
        "3. Сумма чисел.",
        "4. Выход.",
        sep="\n",
    )

    menu_item = input("Выберите пункт меню: ")
    if menu_item == "1":
        ...  # TODO: реализовать _4_practice.py
    elif menu_item == "2":
        number = int(input("Enter n: "))
        result = 1

        tmp = number
        while tmp > 1:
            result *= tmp
            tmp -= 1

        print("!", number, " = ", result, sep="")
        input("Press Enter to Continue...")

    elif menu_item == "3":
        count = 0
        while True:
            number_1 = random.randint(1, 10)
            number_2 = random.randint(1, 10)

            print(number_1, "+", number_2, "=", end=" ")
            answer = int(input())

            if answer == number_1 + number_2:
                count += 1
            else:
                print("Game over:", count)
                break
        input("Press Enter to Continue...")

    elif menu_item == "4":
        print("Bye!")
        break
