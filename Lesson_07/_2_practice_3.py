"""
    Через пробел вводятся слова.
    1. Сформировать список.
    2. Найти самое длинное и самое короткое слово списка.
    3. Поменять их местами.
    4. Вывести в консоль: исходный список, найденные слова, итоговый список.
"""


def main():
    # 1. Сформировать список.
    my_list = input("Введите слова через пробел: ").split()
    my_copy = my_list.copy()

    # 2. Найти самое длинное и самое короткое слово списка.
    longest = shortest = my_copy[0]
    for word in my_copy[1:]:
        if len(word) > len(longest):
            longest = word
        if len(word) < len(shortest):
            shortest = word

    # либо можно воспользоваться min/max + key
    longest = max(my_copy, key=len)
    shortest = min(my_copy, key=len)

    print(longest, shortest)

    # 3. Поменять их местами.
    idx_l = my_copy.index(longest)
    idx_s = my_copy.index(shortest)

    my_copy[idx_l], my_copy[idx_s] = my_copy[idx_s], my_copy[idx_l]

    print(my_copy)

    # 4. Вывести в консоль: исходный список, найденные слова, итоговый список.
    print(
        f"Исходный список: {my_list}\n"
        f"Самое длинное слово: {longest}\n"
        f"Самое короткое слово: {shortest}\n"
        f"Итоговый список: {my_copy}"
    )


if __name__ == "__main__":
    main()
