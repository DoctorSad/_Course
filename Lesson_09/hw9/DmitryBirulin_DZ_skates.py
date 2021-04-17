"""
    В прокате коньков есть разные размеры. Известно, что желающий покататься
    может надеть коньки любого размера, которые не меньше размера его ноги.

    Напишите функцию, которая принимает список доступных размеров коньков и
    список размеров ног желающих.

    И возвращает наибольшее количество людей,
    которые смогут покататься одновременно.


    Например:
    [in]
    [39, 38, 41, 37] (доступные размеры)
    [40, 39, 41] (размеры ног желающих)

    [out]
    2

    [37, 38, 39, 40] , [37, 37, 40, 40] -> 3
    [37, 38, 39, 40] , [42] -> 0
    [37, 38, 39] , [37, 37, 37, 37] -> 3

    Напишите несколько тестов
"""


# def main():
    # print('Введите список доступных размеров коньков: ')
    # available_sizes_in = input()
    # print('Введите список замеров ног желающих: ')
    # foot_sizes_in = input()
    # out = skates(available_sizes_in, foot_sizes_in)
    # print(out)


def skates(available_sizes_, foot_sizes_):
    import re
    available_sizes = re.findall(r"[0-9]+", available_sizes_)
    foot_sizes = re.findall(r"[0-9]+", foot_sizes_)
    max_pairs = 0
    available_sizes.sort()
    foot_sizes.sort(reverse=True)
    for i in foot_sizes:
        if len(foot_sizes) and len(available_sizes):
            if int(i) <= int(available_sizes[-1]):
                foot_sizes = foot_sizes[1:]
                available_sizes.pop()
                max_pairs += 1
    return max_pairs


assert skates('37 38 39 40', '37 37 40 40') == 3
assert skates('k, 1', 'z') == 0
assert skates('37, 38, 39, 40', '42') == 0
assert skates('37, 38, 39', '37, 37, 37, 37') == 3
assert skates('39, 38, 41, 37', '40, 39, 41') == 2
print("All tests passed successfully!")

#
# if __name__ == "__main__":
#     main()
