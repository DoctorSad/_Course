"""
    Написать функцию, которая принимает список строк,
    и возвращает другой список, содержащий все самые длинные строки.

    Например:
    [in] ['a', 'asd', 'bd', 'q', 'dsq']
    [out] ['asd', 'dsq']
"""


def main():
    print(longest_strings(['a', 'asd', 'bd', 'q', 'dsq']))


def longest_strings(list_in: list) -> list:
    """ Функция возвращает список самых длинных строк из списка list_in """
    list_out = []
    max_len = 0
    for i in list_in:
        if len(i) > max_len:
            max_len = len(i)
    for i in list_in:
        if len(i) == max_len:
            list_out.append(i)
    return list_out


t_1 = ["x"]
assert longest_strings(t_1) == ["x"]

t_2 = ["abc", "eeee", "abcd", "dcd"]
assert longest_strings(t_2) == ["eeee", "abcd"]

t_3 = ["a", "abc", "cbd", "zzzzzz", "a", "abcdef", "asasa", "aaaaaa"]
assert longest_strings(t_3) == ["zzzzzz", "abcdef", "aaaaaa"]

t_4 = ["enyky", "benyky", "yely", "varennyky"]
assert longest_strings(t_4) == ["varennyky"]

t_5 = ["abacaba", "abacab", "abac", "xxxxxx"]
assert longest_strings(t_5) == ["abacaba"]

print("All tests passed successfully!")


if __name__ == "__main__":
    main()
