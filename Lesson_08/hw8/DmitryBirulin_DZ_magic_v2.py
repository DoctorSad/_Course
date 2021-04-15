"""
    Реализуйте игру Magic (hw3/magic.py) с некоторыми дополнениями.

    1. При запуске, программа спрашивает имя игрока.

    2. В словаре player_data хранить данные игрока и актуализировать их после
    каждой сыгранной игры. Оперировать такими данными:
        name - имя игрока
        games - общее количество сыграных игр
        record - рекордное количество попыток (минимальное)
        avg_attempts - среднее количество попыток за игру

    3. При выходе из программы данные игрока записывать в файл (txt либо json).

    **4. При запуске программы, после ввода имени пользователем, читать файл,
    если данные об игроке есть в файле то загружать их в player_data.

"""

import random
from pathlib import Path
import json


def main():
    BASE_DIR = Path(__file__).resolve().parent
    FILES_DIR = BASE_DIR / "Files"
    FILES_DIR.mkdir(exist_ok=True)
    file_path = FILES_DIR / "player_data.json"

    player_data = {}
    print('Введите имя игрока: ')
    player_name = input()

    with open(file_path) as f:
        player_data_in = json.load(f)
        for i in player_data_in:
            if i['name'] == player_name:
                player_data = i
                new_player = False
                break
            else:
                player_data = {'name': player_name, 'games': 0, 'record': 9999, 'avg_attempts': float(1)}
                new_player = True
    while True:
        tmp_data = magic()
        player_data_out = []
        player_data['games'] += 1
        if player_data['record'] > tmp_data['record']:
            player_data['record'] = tmp_data['record']
        player_data['avg_attempts'] = round(((player_data['avg_attempts'] * (player_data['games'] - 1) +
                                              tmp_data['attempts']) / player_data['games']), 2)
        if new_player:
            player_data_in.append(player_data)
            player_data_out = player_data_in
        else:
            for i in player_data_in:
                if i['name'] != player_name:
                    player_data_out.append(i)
                else:
                    player_data_out.append(player_data)
        out = input('                                    Continue (Y/n)?: ')
        if out == 'n':
            print('Bye!')
            break

    with open(file_path, "w") as f:
        data = json.dumps(player_data_out, indent=4)
        f.write(data)


def magic() -> dict:
    while True:
        count = 1
        guess = None
        record = 1000000
        print('Введите нижний диапазон: ', end='')
        min_ = input()
        print('Введите верхний диапазон: ', end='')
        max_ = input()
        try:
            min_ = int(min_)
            max_ = int(max_)
        except ValueError:
            print('Вы не ввели диапазоны с типом <int>')
        else:
            magic_number = random.randint(min_, max_)
            while not guess:
                print('Введите число: ', end='')
                try:
                    number = int(input())
                except ValueError:
                    print('Вы не ввели число типа <int>')
                    break
                if number > magic_number:
                    print('Вы ввели число которое больше рандомного')
                    count += 1
                elif number < magic_number:
                    print('Вы ввели число которое меньше рандомного')
                    count += 1
                elif number == magic_number:
                    print('Вы угадали рандомное число <', magic_number, '>. Использовано попыток: ', count)
                    if count < record:
                        print('Вы установили новый рекорд!')
                        record = count
                    guess = 1
            return {'record': record, 'attempts': count}


if __name__ == "__main__":
    main()