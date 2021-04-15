# 1. Отобразите элементы, которые не являются общики для списков
# Ожидаемый результат: {40, 10, 50, 30}
list_1 = {10, 20, 30}
list_2 = {20, 40, 50}

print((list_1.symmetric_difference(list_2)))

# 2. Удалите 10, 20 и 30 из set_2
# Ожидаемый результат: {40, 50}
set_1 = {10, 20, 30, 40, 50}

set_tmp1 = {10, 20, 30}
print(set_1.difference(set_tmp1))

# 3. Проверьте, если у множеств общие элементы и если есть, выведите на экран
set_1 = {10, 20, 30, 40, 50}
set_2 = {60, 70, 80, 90, 10}

print(set_1.intersection(set_2))

# 4. Удалите из set_1 элементы, которые не являются общими для set_1 и set_2
# Ожидаемый результат: {40, 50, 30}
set_1 = {10, 20, 30, 40, 50}
set_2 = {30, 40, 50, 60, 70}

# variant #1
# set_1 = set_1.intersection(set_2)
# print(set_1)

# variant #2
print(set_1 - (set_1 - set_2))

# 5. Добавьте элементы списков list_1 и list_2 в множество set_1
# Ожидаемый результат: {'reg', 'green', 'black', 'white', 'yellow', 'gray', 'blue'}
set_1 = {"reg", "green", "blue"}

list_1 = ["white", "gray", "black"]
list_2 = ["blue", "yellow"]

set_1.update(set(list_1))
set_1.update(set(list_2))
print(set_1)
