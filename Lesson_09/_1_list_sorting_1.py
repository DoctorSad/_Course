"""
    Сортировка списка словарей по ключу.

    sorted(iter, key=func)
    list.sort(key=func)

    В функцию sorted() либо метод списка .sort() можно передать функцию func,
    которая будет применяться к каждому элементу последовательности
    при сортировке.

    Можно передавать обычную функцию либо использовать lambda выражения.
"""

data = [
    {
        "name": "Kate",
        "email": "kate@gmail.com",
        "bday": "19.10.1999",
        "country": "Germany",
    },
    {
        "name": "John",
        "email": "john@gmail.com",
        "bday": "19.10.1997",
        "country": "USA",
    },
    {
        "name": "ann",
        "email": "ann@gmail.com",
        "bday": "19.10.1998",
        "country": "Ukraine",
    },
    {
        "name": "ann",
        "email": "ann@gmail.com",
        "bday": "19.10.1998",
        "country": "France",
    },
]


def main():
    # 1. Остортировать список по имени ('name')
    print("1.", sorted(data, key=sort_by_name))

    # 2. Остортировать список по стране ('country')

    # 3. Остортировать список по имени и стране ('name' и 'country')


def sort_by_name(data):
    # функция принимает словарь и возвращает значение по ключу 'name'
    return data["name"].lower()


if __name__ == "__main__":
    main()
