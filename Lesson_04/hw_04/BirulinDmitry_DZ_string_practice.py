string = "Lorem, Ipsum, is, simply, dummy, text, of, the, printing, industry."

# 1. Удалить из строки символы ','.
#    Результат: 'Lorem Ipsum is simply dummy text of the printing industry.'

print(string.replace(',', ''))

# 2. Найти индекс самой последней буквы 'i' в строке.
#    Результат: 54

print(string.rfind('i'))  # правильно 58!

# 3. Найти количество букв 'i' в строке (регистр не имеет значения).
#    Результат: 6

print(string.lower().count('i'))

# 4. Найти и вывести срез строки от 3 буквы 's' до 6 пробела.
#    Результат: 'simply dummy text'
#    (используйте методы find или index для получения индексов, вторым
#     параметром можно передать индекс, от которого делать поиск find('s', 12))

s_third = string.find('s', string.find('s', string.find('s') + 1) + 1)
space_six = string.find(' ', string.find(' ', string.find(' ', string.find(' ', string.find(' ', string.find(' ') + 1) + 1) + 1) +1) +1)
print(string[s_third:space_six])  # правильно с учетом запятой в конце и с учетом запятых по ходу строки


# 5. Продублируйте первую половину строки 3 раза и склейте с второй половиной
#    и выведите на экран.
#    Результат: 'Lorem Ipsum is simply dummy tLorem Ipsum is simply dummy tLorem Ipsum is simply dummy text of the printing industry.'

print(string[:int(len(string) / 2) + 1] * 3 + string[int(len(string) / 2) + 1:])  # результат в комментарии неправильный, отсутствуют запятые
