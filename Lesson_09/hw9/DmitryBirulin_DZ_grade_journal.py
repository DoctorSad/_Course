"""
    Пользователь вводит количество студентов N.
    После чего вводит N строк, в которых записана фамилия и балл через пробел.

    Программа выводит список фамилий, отсортированный по их баллам по убыванию.

    Пример:

    [out] Введите количество студентов:
    [in]  3

    [out] Введите фамилию и балл:
    [in]  Иванов 87

    [out] Введите фамилию и балл:
    [in]  Смирнов 90

    [out] Введите фамилию и балл:
    [in]  Фролов 89

    [out]
        1. Смирнов
        2. Фролов
        3. Иванов
"""


def main():
    import re
    while True:
        print('Введите количество студентов: ')
        temp = input()
        data = []
        number_of_students = re.findall(r"[0-9]+", temp)
        if not len(number_of_students):
            print('Введите корректное количество студентов.')
        else:
            if int(number_of_students[0]) > 0:
                for i in range(int(number_of_students[0])):
                    print('Введите фамилию и балл: ')
                    values = input()
                    surname = str(''.join(re.findall(r"[a-zA-ZА-Яа-я]+", values))).title()
                    score = int(''.join(re.findall(r"[0-9]+", values)))
                    one_student = {'surname': surname, 'score': score}
                    data.append(one_student)
            data.sort(key=lambda x: x['score'], reverse=True)
            count = 1
            print('\nCписок фамилий, отсортированный по их баллам по убыванию: ')
            for i in data:
                print(f'{count}. {i["surname"]}')
                count += 1
            if not exit_program():
                break


def exit_program() -> int:
    out = input('                                    Заполнить еще одну форму регистрации (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
        return 1  # Продолжаем программу
    else:
        return 0  # Заканчиваем программу


if __name__ == "__main__":
    main()
