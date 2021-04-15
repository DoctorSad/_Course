"""
    Дан файл с информацией о пользователях _0_practice_dict_0.txt

    Формат данных:
    имя фамилия возвраст страна

    Создайте структуру с данными используя списки и словари
"""
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).resolve().parent / "_0_practice_dict_0.txt"


def main():
    data = []

    fields = ["name", "surname", "age", "country"]

    with open(file_path) as f:
        for line in f.readlines():

            # user_data = line.split()
            # user_dict = {
            #     "name": user_data[0],
            #     "surname": user_data[1],
            #     "age": user_data[2],
            #     "country": user_data[3],
            # }
            user_dict = dict(zip(fields, line.split()))
            data.append(user_dict)

    pprint(data)
    for user in data:
        print(user["name"])


if __name__ == "__main__":
    main()
