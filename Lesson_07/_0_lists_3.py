"""
    Сортировка, реверс, max/min.
"""


def main():
    numbers = [8, 6, -12, 21, 32, -5, 7, 16]

    # Минимальное и максимальное значение списка с помощью min() и max()
    print("min =", min(numbers))
    print("max =", max(numbers))

    # Сумма чисел списка
    print("sum =", sum(numbers))

    words = ["g", "s", "S", "s", "1", "u", "W", "a", "0"]

    # Сортировка с помощью sorted возвращает отсортированный список
    # sorted(list[, key[, reverse]])
    print(sorted(words))
    print(sorted(words, reverse=True))
    print(words)

    # reversed() возвращает реверс списка (итератор)
    print(list(reversed(numbers)))
    print(numbers)


if __name__ == "__main__":
    main()
