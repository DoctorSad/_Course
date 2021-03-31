"""
    Программу принимает на ввод строку string и число n.
    Выводит на экран строку с смещенными символами на число n.

    В результате должно получится 4 функции:
    - main
    - функция для получения не пустой строки.
    - функция для получения сдвига (целое число).
    - функция, которая делает сдвиг строки.

    Пример:
    Введите строку: python hello world
    Введите сдвиг: 5

    Результат: n hello worldpytho

    Введите строку: python hello world
    Введите сдвиг: -2

    Результат: ldpython hello wor

    * используйте индексы, срезы и возможно циклы
"""


def main():
    while True:
        input_string = ''
        output_string = None
        shift = 0
        print('Введите строку: ', end='')
        input_string = input()
        while True:
            print('Введите параметр сдвига: ', end='')
            shift = input()
            try:
                shift = int(shift)
            except ValueError:
                print('Вы не ввели диапазоны с типом <int>')
                continue
            else:
                break
        output_string = string_shift(input_string, shift)
        print(output_string)
        if exit_program():
            continue
        else:
            break


def string_shift(input_string: str, shift: int) -> str:
    output_string = None
    if shift == 0:
        output_string = input_string
        print(output_string)
    elif len(input_string) == 0:
        print('Введена строка с нулевой длиной')
    elif abs(shift) > len(input_string):
        print('Сдвиг больше чем длина сроки!')
    elif shift == len(input_string):
        output_string = input_string
    elif shift > 0:
        output_string = input_string[len(input_string) - shift:] + input_string[:len(input_string) - shift]
    elif shift < 0:
        output_string = input_string[-1 * shift:] + input_string[:-1 * shift]
    return output_string


def exit_program() -> int:
    out = input('                                    Продолжаем (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
        return 1  # Продолжаем программу
    else:
        return 0  # Заканчиваем программу


if __name__ == "__main__":
    main()
