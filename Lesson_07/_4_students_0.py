"""
    1. Программа принимает на ввод имена студентов.
    2. Необходимо сохранить данные в переменную.
    3. Отсортировать список по алфавиту в обратном порядке.
    4. Вывести порядковый номер и содержимое для каждого элемента списка.
"""


def main():
    students = []  # список для хранения имен

    for i in range(5):
        student = input(f"Введите имя студента #{i+1}: ").strip().title()
        students.append(student)

    students.sort(reverse=True)

    # если буквы в строках разного регистра стоит применить key=str.casefold
    # students.sort(key=str.casefold, reverse=True)

    for idx, student in enumerate(students):
        print(f"{idx + 1}. {student}")


if __name__ == "__main__":
    main()
