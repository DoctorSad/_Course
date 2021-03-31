def main():
    choice = input(
        "Меню: \n"
        "1. Найти количество четных и нечетных цифр числа.\n"
        "2. Найти факториал числа.\n"
        "3. Выход.\n"
        "Сделайте выбор и нажмите Enter: "
    )
    if choice == "1":
        odd_even()
    elif choice == "2":
        factorial()
    elif choice == "3":
        print("Bye!")
        return

    return main()


def odd_even():
    number = int(input("Ведите число: "))
    tmp = number
    even = 0
    odd = 0

    while number > 0:
        last_digit = number % 10

        if last_digit % 2 == 0:
            even += 1
        else:
            odd += 1

        number //= 10

    print("В числе", tmp, "четных цифр -", even, ", нечетных -", odd)


def factorial():
    number = int(input("Введите число, факториал которого найти: "))
    tmp = number
    factorial = 1
    while number > 1:
        factorial *= number
        number -= 1
    print("!", tmp, " = ", factorial, sep="")


if __name__ == "__main__":
    main()
