"""
    Программу принимает на ввод строку string и число n.
    Выводит на экран строку с смещенными символами на число n.

    Весь код можно написать в одной функции main,
    но рекомендуется разбить код на несколько функций, например:
    - main
    - функция для получения не пустой строки.
    - функция для получения сдвига (целое число).
    - функция, которая делает сдвиг строки.

    Пример:
    Введите строку: python hello world
    Введите сдвиг: 5

    Результат: n hello worldpytho

    Введите строку: python hello world
    Введите сдвиг: -2

    Результат: ldpython hello wor

    * используйте индексы, срезы и возможно циклы
"""


def main():
    string = get_not_empty_string()
    n = get_int()

    print("1", shift(string, n))
    print("2", shift_v2(string, n))
    print("3", shift_v3(string, n))


def get_not_empty_string():
    """Функция для получения не пустой строки"""
    s = input("Введите строку: ")
    if s == "":
        return get_not_empty_string()
    return s


def get_int():
    """Функция для получения целого числа"""
    n = input("Введите сдвиг (целое число): ")
    try:
        n = int(n)
    except ValueError:
        return get_int()
    return n


def shift(string, n):
    """Функция делает сдвиг строки на n элементов"""
    return string[n:] + string[:n]


def shift_v2(string, n):
    """Функция делает циклический сдвиг строки на n элементов
    (n - положительное)"""
    for _ in range(n):
        string = string[1:] + string[:1]
    return string


def shift_v3(string, n):
    """Функция делает циклический сдвиг строки на n элементов"""
    idx = -1 if n < 0 else 1
    for _ in range(abs(n)):
        string = string[idx:] + string[:idx]
        print(string)
    return string


if __name__ == "__main__":
    main()
