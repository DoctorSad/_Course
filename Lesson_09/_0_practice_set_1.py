"""
    Даны списки групп студентов.

    1. Узнать количество уникальных студентов со всех группах.
    2. Вывести на экран список студентов, которые есть во всех группах.
"""


def main():
    group_a = ["Max", "Jane", "John", "Ann", "Julia", "Mary"]
    group_b = ["Ann", "Bob", "Robert", "Sara", "Jane", "Alex"]
    group_c = ["Maria", "Bob", "Jone", "Sara", "Jane", "Alex"]

    unique_students = set(group_a + group_b + group_c)
    print("1.", len(unique_students))

    # Студенты, которые присутствуют во всех группах одновременно
    students = set(group_a) & set(group_b) & set(group_c)
    print("2.", list(students))

    # Студенты, которые есть в группе а и группе b
    students = set(group_a) & set(group_b)
    print(list(students))

    # Список уникальных студентов всех групп через запятую
    print(", ".join(unique_students))


if __name__ == "__main__":
    main()
