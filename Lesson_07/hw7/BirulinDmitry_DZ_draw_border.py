"""
    Нарисовать границу из * в списке.
    Количество элементов каждой строки уравнять по самой длинной в списке,
    центрировать текст и недостающие символы заполнить пробелами.

    [in]    ['python',
             'django']

    [out]   ['********',
             '*python*',
             '*django*',
             '********']

    [in]    ['py',
             'python']

    [out]   ['********',
             '*  py  *',
             '*python*',
             '********']

    Покрыть несколькими тестами.
"""

from pprint import pprint


def main():
    list = draw_border(['pyqwewer',
       'python11111111111111111111111',
       ' ',
                        '1234'])
    pprint(list[1], width=list[0] + 8)


def draw_border(input_list: list) -> list:
    list_out = []
    tmp_list = list(input_list)
    max_len = 0
    for i in input_list:
        if len(i) > max_len:
            max_len = len(i)
    tmp_list.append('*' * max_len)
    tmp_list.reverse()
    tmp_list.append('*' * max_len)
    tmp_list.reverse()
    for i in tmp_list:
        if len(i) < max_len - 2:
            i = i.center(max_len, " ")
        i = i + '*'
        i = i[::-1]
        i = i + '*'
        i = i[::-1]
        list_out.append(i)
    out = [max_len, list_out]
    return out


if __name__ == "__main__":
    main()
