"""
    Сортировка списков различных объектов.

    sorted(iter, key=func)
    list.sort(key=func)

    В функцию sorted() либо метод списка .sort() можно передать функцию func,
    которая будет применяться к каждому элементу последовательности
    при сортировке.

    Можно передавать обычную функцию либо использовать lambda выражения.
"""


def main():
    # 1. Необходимо отсортировать список строк words по алфавиту
    words = ["A", "django", "Zappelin", "BROWN", "black", "advanced"]

    print("1.", sorted(words))
    # ['A', 'BROWN', 'Zappelin', 'advanced', 'black', 'django']

    # результат не совсем очевидный, но сортировка идет по ascii кодам
    # ord('A') == 65; ord('a') == 97

    # для того, чтобы сортировка была правильной,
    # нужно, чтобы все строки были в одном регистре

    print("2.", sorted(words, key=str.casefold))

    # теперь в обратном порядке
    print("3.", sorted(words, key=str.casefold, reverse=True))

    # 2. Отсортировать список слов по их длине

    print("4.", sorted(words, key=len))


if __name__ == "__main__":
    main()
