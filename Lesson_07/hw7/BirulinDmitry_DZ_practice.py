"""
    1. Сгенерировать список случайной длины заполнив его случайными числами
    (используйте random, диапазон чисел произвольный)
    2. Вывести на экран числа из списка в обратном порядке через пробел
    3. Извлечь первое число, возвести его в квадрат и вставить в средину списка
    4. Удалить из списка простые числа.
    5. Записать в файл list_info.txt строчки:
        - 1. элементы списка через запятую
        - 2. количество элементов списка
        - 3. самое маленькое число списка
        - 4. сумму чисел списка кратных 3
"""

import random


def main():

    #  1. Сгенерировать список случайной длины заполнив его случайными числами
    number_of_items = random.randint(10, 20)
    list_of_items = []
    for _ in range(number_of_items):
        list_of_items.append(random.randint(-30, 90))
    print(f'\nИзначальный список: ')
    list_of_items_tmp = list(list_of_items)
    for _ in range(len(list_of_items)):
        print(f'{list_of_items_tmp.pop()} ', end='')

    #  2. Вывести на экран числа из списка в обратном порядке через пробел
    reverse_list(list_of_items)

    #  3. Извлечь первое число, возвести его в квадрат и вставить в средину списка
    first_number_edit(list_of_items)

    #  4. Удалить из списка простые числа.
    del_simple_numbers(list_of_items)

    #  5. Записать в файл list_info.txt строчки
    create_list_info(list_of_items)


def reverse_list(list_of_items: list):
    list_of_items_tmp = list(list_of_items)
    print(f'\n\nЧисла из списка в обратном порядке через пробел: ')
    list_of_items_tmp.reverse()
    for _ in range(len(list_of_items)):
        print(f'{list_of_items_tmp.pop()} ', end='')


def first_number_edit(list_of_items: list):
    list_of_items_out = []
    list_of_items_tmp = list(list_of_items)
    list_of_items_tmp.reverse()
    first_number = list_of_items_tmp.pop()
    list_of_items_tmp.reverse()
    first_number = first_number ** 2
    count = 0
    for i in list_of_items_tmp:
        if count == round(len(list_of_items_tmp) / 2):
            list_of_items_out.append(first_number)
        list_of_items_out.append(i)
        count += 1
    print(f'\n\nИзвлечь первое число, возвести его в квадрат и вставить в средину списка: ')
    for _ in range(len(list_of_items)):
        print(f'{list_of_items_out.pop()} ', end='')


def del_simple_numbers(list_of_items: list):
    list_of_items_out = []
    for i in list_of_items:
        not_simple = 0
        delitel = 2
        if i < 2:
            list_of_items_out.append(i)
            continue
        while delitel < i:
            if not i % delitel:
                not_simple += 1
                if not_simple:
                    break
            delitel += 1
        if not_simple:
            list_of_items_out.append(i)
    print(f'\n\nУдалить из списка простые числа: ')
    for _ in range(len(list_of_items_out)):
        print(f'{list_of_items_out.pop()} ', end='')
    print('\n', end='')


def create_list_info(list_of_items: list):
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent
    FILES_DIR = BASE_DIR / "Files"
    FILES_DIR.mkdir(exist_ok=True)
    file_path = FILES_DIR / "list_info.txt"

    list_of_items_tmp = list(list_of_items)
    sum_items = 0
    for i in list_of_items_tmp:
        if i % 3 == 0:
            sum_items += i
    list_of_items_out = list(list_of_items)
    count = 0
    with open(file_path, "a") as f:
        for _ in list_of_items:
            if count == len(list_of_items) - 1:
                print(f'{list_of_items_out.pop()}', file=f)
                print(f'{len(list_of_items)}', file=f)
                print(f'{min(list_of_items)}', file=f)
                print(f'{sum_items}', file=f)
            else:
                print(f'{list_of_items_out.pop()}, ', end='', file=f)
            count += 1
        print('-' * 50, end='', file=f)
        print('\n', end='', file=f)


if __name__ == "__main__":
    main()
