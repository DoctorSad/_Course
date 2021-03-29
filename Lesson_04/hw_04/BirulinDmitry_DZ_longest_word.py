"""
    1. Вводится строка
    2. Программа считает количество слов в введенной строке и выводит на экран.
    2. Программа определяет самое длинное слово и его длину и выводит на экран.
    ___________________________________________________________________________

    Например:

   # >>> Hello,world! I am learning python.

    Слов в введенной строке: 6
    Самое длинное слово: "learning" (8 символов)

"""
out_str = []
count = 0
max_ = 0
longest_word = ''

while True:
    for _ in range(20):
        print('\n')
    print('     *** Longest word ***     ')
    input_string = input('Введите строку: ')
    string_punctuation = ',. '
    temp_string = ''
    input_string += ' '
    for i in input_string:
        if string_punctuation.find(i) == -1:
           temp_string += i
           count = 0
        elif bool(string_punctuation.count(i)) and count == 0:
            count += 1
            out_str.append(temp_string)
            temp_string = ''
    for i in out_str:
        if max_ < len(i):
            max_ = len(i)
            longest_word = i
    print('Слов в введенной строке: ', len(out_str))
    print(f'Самое длинное слово: "{longest_word}"')
    out = input('                                    Будем вводить новую строку (Y/n)?: ')
    if not out or out == 'Y':
        for _ in range(20):
            print('\n')
        out_str.clear()
        longest_word = ''
        max_ = 0
        count = 0
        continue
    elif out == 'n':
        break
