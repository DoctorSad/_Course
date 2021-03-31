"""
    Необходимо написать программу, которая принимает на ввод 2 целых числа.
    Считает сумму чисел в отдельной функции.
    Если сумма больше 0, то вызывается функция positive,
    которая выводит сообщение 'positive',
    если меньше - функция negative, которая выводит сообщение negative.

"""


def main():
    a = float(input("a: "))
    b = float(input("b: "))

    result = sum_(a, b)
    if result > 0:
        positive()
    elif result < 0:
        negative()


def sum_(a: float, b: float) -> float:
    return a + b


def positive():
    print("positive")


def negative():
    print("negative")


if __name__ == "__main__":
    main()
