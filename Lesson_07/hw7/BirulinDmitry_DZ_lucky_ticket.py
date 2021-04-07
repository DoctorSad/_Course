"""
    Написать функцию, которая будет проверять счастливый билетик или нет.

    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
    Если количество цифр одной и второй половины не равно - билет не счастливый
"""


def main():
    print(is_lucky(123456456321))


def is_lucky(ticket_num: int) -> bool:
    if len(str(ticket_num)) % 2 != 0:
        return False
    ticket_num_str = str(ticket_num)
    middle = int(len(ticket_num_str) / 2)
    first_number = ticket_num_str[:middle]
    second_number = ticket_num_str[middle:]
    sum_first = 0
    sum_second = 0
    for i in first_number:
        sum_first = sum_first + int(i)
    for i in second_number:
        sum_second = sum_second + int(i)
    if sum_first == sum_second:
        return True
    return False



assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True
assert is_lucky(4799731) is False
assert is_lucky(1379974) is False

print("All tests passed successfully!")


if __name__ == "__main__":
    main()
