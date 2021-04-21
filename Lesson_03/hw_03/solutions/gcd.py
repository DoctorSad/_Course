"""
    Алгоритм Евклида. НОД - наибольший общий делитель

    1. Большее число делим на меньшее.
    2. Если делится без остатка, то меньшее число и есть НОД (выходим из цикла)
    3. Если есть остаток, то большее число заменяем на остаток от деления.
    4. Переходим к 1 пункту.

"""

# 1
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# при вводе отрицательных чисел зацикливается
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)


# 2
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
while b > 0:
    a, b = b, a % b

print("Наибольший общий делитель:", a)


# 3
a = int(input("введіть число а: "))
b = int(input("введіть число b: "))

while True:
    max_number = max(a, b)
    min_number = min(a, b)
    rem = max_number % min_number

    if rem == 0:
        print(min_number)
        break
    elif rem > 0:
        if a > b:
            a = rem
        else:
            b = rem

# 5
while True:
    for _ in range(20):
        print("\n")
    print("*** Алгоритм Евклида ***".center(34))
    num_1 = input("Введите первое число: ")
    num_2 = input("Введите второе число: ")
    tmp_1 = None
    tmp_2 = None

    try:
        tmp_1 = int(num_1)
        tmp_2 = int(num_2)
    except ValueError:
        print("Не введены два числа для вычислений")
    else:
        while True:
            if not tmp_1 or not tmp_2:
                nod = tmp_1 + tmp_2
                print("\nНаибольший общий делитель: ", nod)
                break
            elif tmp_1 == tmp_2:
                print("\nНаибольший общий делитель: ", tmp_1)
                break
            elif tmp_1 > tmp_2:
                tmp_1 %= tmp_2
            elif tmp_2 > tmp_1:
                tmp_2 = tmp_2 % tmp_1

    out = input("Новая пара чисел (Y/n)?: ".rjust(60))
    if not out or out == "Y":
        for _ in range(20):
            print("\n")
        continue
    elif out == "n":
        break
