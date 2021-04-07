def main():
    # Создать список с квадратами чисел списка old_list
    old_list = [1, 2, 3, 4, 5]

    new_list = []
    for i in old_list:
        new_list.append(i ** 2)

    print(old_list)
    print(new_list)

    # с помощью конструктора
    new_list = [i ** 2 for i in old_list]

    print(new_list)


if __name__ == "__main__":
    main()
