def main():
    my_list = [1, -2, 16, -13, 20, 0, 3, 77, 225, -42, -10, 21, 523]

    # 1.
    # Поменять местами 1 и последний элемент списка.
    my_list[0], my_list[-1] = my_list[-1], my_list[0]

    # 2.
    # Создать новый список состоящий из элементов my_list, при этом заменив
    # отрицательные числа на -1,
    # положительные - на число 1, ноль оставить без изменений.
    # Вывести 2 списка.
    new_list = []
    for i in my_list:
        if i < 0:
            i = -1
        elif i > 0:
            i = 1

        new_list.append(i)

    print(my_list, new_list)

    # 3.
    # Разделить исходный список на два списка
    # с положительными и отрицательными числами.
    # Вывести максимальное и минимальное значение каждого списка.

    positives = []
    negatives = []
    for i in my_list:
        if i < 0:
            negatives.append(i)
        elif i > 0:
            positives.append(i)

    print(max(positives), min(positives))
    print(max(negatives), min(negatives))

    # 4.
    # Создайте список,
    # в котором содержатся только нечетные числа из списка my_list

    new_list = [i for i in my_list if i % 2 != 0]

    # 5.
    # Создайте список,
    # в котором содержатся квадраты отрицательных чисел из списка my_list

    new_list = [i ** 2 for i in my_list if i < 0]
    print(new_list)


if __name__ == "__main__":
    main()
