def main():
    colors = [
        (2, "green"),
        (1, "blue"),
        (2, "yellow"),
        (1, "Aquamarine"),
        (4, "red"),
        (3, "gold"),
        (5, "black"),
        (2, "Brown"),
        (5, "pink"),
        (1, "purple"),
        (4, "white"),
        (1, "gray"),
    ]

    # 1. Вывести список colors, отсортированный по цвету (2 элемент кортежа).

    colors.sort(key=lambda x: str(x[1]).casefold())
    print(colors)

    # 2. Отсортировать список по 1 и 2элементу кортежа.
    # Результат вывести на экран.

    colors.sort(key=lambda x: (x[0], str(x[1]).casefold()))
    print(colors)

    # 3. С помощью filter() и lambda вывести только те кортежи из списка,
    # цвет которых начинается на букву 'b'

    print(list(filter(lambda x: x[1][:1] == 'b', colors)))

    # 4. Вывести цвет, которой состоит из найбольшего количества букв.

    print(max(colors, key=lambda x: len(x[1])))

    # 5. Создайте словарь с ключами 'long' и 'short'.
    # Значение ключа 'long' - список кортежей, длина цвета которых > 4 символов
    # Значение ключа 'short' - список оставшихся кортежей

    list_of_long = list(filter(lambda x: len(x[1]) > 4, colors))
    list_of_short = list(filter(lambda x: len(x[1]) <= 4, colors))
    print(dict(zip(['long', 'short'], [list_of_long, list_of_short])))


if __name__ == "__main__":
    main()
