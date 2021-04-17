"""
    В файле data.json даны значения температур в гразусах C, F и K.
    У каждой ячейки есть номер рядка 'row' и номер колонки 'col'.

    1. Реализуйте функцию parse_data, которая читает файл,
    приводит содержимое к python объекту (json.load), возвращает список.

    2. Реализуйте функцию sort_data, которая принимает список,
    сортирует по ключу 'row' и 'col' и возвращает его.

    3. Реализуйте функцию show_data, которая выводит отсортированную таблицу
    градусов в любом удобном для чтения формате

    Пример вывода:
    °C     °F     °K
    100.0  212.0  373.15
    90.0   194.0  363.15
    80.0   176.0  353.15
    ...

    Еще пример вывода:
    °C    | °F    | °K
    ----------------------
    100.0 | 212.0 | 373.15
    90.0  | 194.0 | 363.15
    80.0  | 176.0 | 353.15
    ...

    Еще пример вывода:
    №  | °C    | °F    | °K
    ---------------------------
    1  | 100.0 | 212.0 | 373.15
    2  | 90.0  | 194.0 | 363.15
    3  | 80.0  | 176.0 | 353.15
    ...

"""


from pathlib import Path
import json
from pprint import pprint


def main():
    data = parse_data('Files', 'data.json')
    data = sort_data(data)
    show_data(data)


def parse_data(dir_: str, file: str) -> list:
    BASE_DIR = Path(__file__).resolve().parent
    FILES_DIR = BASE_DIR / dir_
    FILES_DIR.mkdir(exist_ok=True)
    file_path = FILES_DIR / file
    with open(file_path) as f:
        data = json.load(f)
    return data


def sort_data(list_data: list) -> list:
    list_data.sort(key=lambda x: (x['row'], x['col']))
    return list_data


def show_data(list_data: list):
    print(f'{"-" * 41}')
    print(f'| {"№".ljust(4)} | {"°C".center(8)} | {"°F".center(8)} | {"°K".center(8)} |')
    print(f'{"-" * 41}')
    list_data.sort(key=lambda x: (x['row']), reverse=True)
    number_of_elements = list_data[0]['row']
    count = 1
    for _ in range(number_of_elements):
        temp_list = list(filter(lambda x: x['row'] == count, list_data))
        print(f'| {str(count).ljust(4)} | {str(temp_list[0]["data"]).center(8)} ', end='')
        print(f'| {str(temp_list[1]["data"]).center(8)} | {str(temp_list[2]["data"]).center(8)} | ')
        count += 1
    print(f'{"-" * 41}')


if __name__ == "__main__":
    main()
