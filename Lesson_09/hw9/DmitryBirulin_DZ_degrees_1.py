"""
    В дополнение к degrees_0 реализуйте функцию make_mistakes,
    которая принимает список словарей и в к каждом рядке в случайной колонке
    заменяет значение на 0 либо '?'.

    1. Создайте список данных, используя функцию parse_data из degrees_0
    2. Отсортируйте данные используя функцию sort_data из degrees_0
    3. Повредите данные функцией make_mistakes
    4. Выведите результат с помощью функции show_data из degrees_0

    Пример вывода результата:
    °C     °F     °K
    0      212.0  373.15
    90.0   194.0  0
    80.0   0      353.15
    ...
"""

import random
from pprint import pprint
from DmitryBirulin_DZ_degrees_0 import parse_data
from DmitryBirulin_DZ_degrees_0 import sort_data
from DmitryBirulin_DZ_degrees_0 import show_data


def main():
    data = parse_data('Files', 'data.json')
    data = sort_data(data)
    pprint(data)
    out = make_mistakes(data)
    show_data(out)


def make_mistakes(list_data: list):
    list_data.sort(key=lambda x: (x['row']), reverse=True)
    number_of_elements = list_data[0]['row']
    list_data.sort(key=lambda x: (x['row'], x['col']))
    count = 1
    for data in range(number_of_elements):
        random_item = random.randint(0, 2)
        tmp = list(filter(lambda x: x['row'] == count,  list_data))
        tmp[random_item]['data'] = 0
        count += 1
    return list_data


if __name__ == "__main__":
    main()