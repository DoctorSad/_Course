"""
    Реализовать декораторы:
    1. @time_decorator - считает и выводит время работы функции,
        если функция выполняется дольше 5 секунд, тогда дополнительно
        выводить сообщение print(f'{func.__name__} - very slow function')

    * в func.__name__ лежит название функции

    2. @slow_decorator - замедляет выполнение функции на 5 секунд

    Используйте библиотеку time, а именно функции time и sleep

"""

import time
import sys


def time_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # вызывается задекорированная функция
        if result > 5:
            print(f'Функция {func.__name__} выполнялась больше 5-ти секунд. ENTER для продолжения...')
            input()
        else:
            print(f'Функция {func.__name__} выполнялась меньше 5-ти секунд. ENTER для продолжения...')
            input()
        return result
    return wrapper


def slow_decorator(func):
    def wrapper(*args, **kwargs):
        time_ = 6
        for remaining in range(time_, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d}".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
        result = func(*args, **kwargs)  # вызывается задекорированная функция
        return result
    return wrapper


def second(in_sec: int):
    start = time.time()
    time.sleep(in_sec)
    end = time.time()
    print(f'Время выполнения тела функции (в секундах): {int(end - start)}')
    return end - start


print('\n\n@time_decorator (выполнение функции меньше 5-ти секунд): ')
time_decorator(second)(4)

print('\n\n@time_decorator (выполнение функции больше 5-ти секунд): ')
time_decorator(second)(6)

print('\n\n@slow_decorator (выполнение функции 1 секунда, замедление выполнения на 5 секунд): ')
slow_decorator(second)(1)
