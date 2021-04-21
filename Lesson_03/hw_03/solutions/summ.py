"""
    Пользователь вводит начало и конец числового ряда.
    Если начало не введено - считать, что это 0.

    1. Программа считает и выводит на экран сумму числового ряда.
    2. Произведение нечетных чисел числового ряда.

    * обработать возможные ошибки
"""

start = input("Enter start (optional): ")
end = input("Enter end: ")

try:
    start = int(start) if start else 0
    # start = int(start or 0)
    end = int(end)
except ValueError:
    print("You need to enter numbers.")
else:
    summ, mul = 0, 1
    for i in range(start, end + 1):
        summ += i
        if i % 2 != 0:
            mul *= i

    print("1.", summ)
    print("2.", mul)
