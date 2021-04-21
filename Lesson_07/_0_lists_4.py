"""
    Обход списка в цикле.
"""
from pprint import pprint


def main():
    colors = ["red", "yellow", "orange", "green", "blue", "violet"]

    # Обход элементов циклом for
    for color in colors:
        print(color)

    # Обход индексов
    for i in range(len(colors)):
        print(colors[i])

    # получение индекса и элемента с помощью enumerate
    for idx, color in enumerate(colors):
        print(f"{idx + 1}. {color}")

    # Обход циклом вложенных списков
    matrix = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
    ]
    for i in matrix:
        for j in i:
            print(j)

    # Для вывода структур данных на экран можно использовать pprint
    pprint(matrix, width=25)  # width - максимальное количество символов строки


if __name__ == "__main__":
    main()
