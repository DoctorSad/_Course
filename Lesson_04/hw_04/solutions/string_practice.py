string = "Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry."

# 1. Удалить из строки символы ','.
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

string = string.replace(",", "")
print("1.", string)


# 2. Найти индекс самой последней буквы 'i' в строке.
#    Результат: 49

i_idx = string.rfind("i")
print("2.", i_idx)

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

i_count = string.casefold().count("i")
print("3.", i_count)


# 4. Найти и вывести срез строки от 3 буквы 's' до 6 пробела.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов, вторым
#     параметром можно передать индекс, от которого делать поиск find('s', 12))

s_idx = string.find("s")
for _ in range(2):
    s_idx = string.find("s", s_idx + 1)

space_idx = string.find(" ")
for _ in range(5):
    space_idx = string.find(" ", space_idx + 1)

print("4.", string[s_idx:space_idx])


# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

center = len(string) // 2
result = string[:center] * 3 + string[center:]
print("5.", result)
