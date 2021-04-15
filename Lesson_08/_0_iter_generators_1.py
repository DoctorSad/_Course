"""
    Объекты, элементы которых можно перебирать в цикле for, содержат в себе
    объект итератор. Для того, чтобы его получить необходимо использовать
    функцию iter(), а для извлечения следующего элемента – функцию next().
"""
import time


def first():
    big_list = [i for i in range(10 ** 8)]  # конструктор списка

    for i in big_list:
        print(i)
        if i == 10:
            break


def second():
    big_gen = (i for i in range(10 ** 8))  # генератор

    for i in big_gen:
        print(i)
        if i == 10:
            break

    print(next(big_gen))
    print(next(big_gen))
    print(next(big_gen))
    print(next(big_gen))
    print(next(big_gen))


def time_it():
    start = time.time()
    big_list = [i for i in range(10 ** 8)]
    print("1.", time.time() - start, "seconds")

    start = time.time()
    big_gen = (i for i in range(10 ** 8))
    print("2.", time.time() - start, "seconds")


time_it()
