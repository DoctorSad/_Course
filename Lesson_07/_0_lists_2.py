"""
    Операции со списками.
"""


def main():
    numbers = [1, 2, 3, 4, 5]

    # 1. копирование списков
    numbers_copy = list(numbers)
    numbers_copy_2 = numbers[:]
    numbers_copy_3 = numbers.copy()

    # этот вариант создает ссылку на тот же объект
    numbers_link = numbers

    numbers_copy[0] = "copy"
    numbers_link[0] = "linked"

    print(
        f"1. \tИсходный список: {numbers}\n"
        f"\tКопия: {numbers_copy}\n"
        f"\tСсылка: {numbers_link}"
    )

    # 2. Сложение списков
    concat = numbers_copy + numbers_link
    print(f"2. \t{concat}")

    # 3. Дублирование списков
    dupl = numbers * 5
    print(f"3. \t{dupl}")


if __name__ == "__main__":
    main()
