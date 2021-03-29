"""
    2. Если в строке каждое слово начинается с заглавной буквы, тогда
        добавить в начало строки 'done. '.
        Иначе заменить первые 5 элементов строки на 'draft: '.
    (можно использовать метод replace и/или конкатенацию строк + срезы)

"""

# можно заменить данную строку на input()
string = "Lorem, Ipsum, is, sImPlY, duMMy, TEXT, of, The, printing, INDUSTRY."

out_str = []
count = 0
max_ = 0
break_operation = 0

for _ in range(20):
    print('\n')
my_string = input('Введите строку: ')
string_punctuation = ',. '
temp_string = ''
my_string += ' '
for i in my_string:
    if string_punctuation.find(i) == -1:
       temp_string += i
       count = 0
    elif bool(string_punctuation.count(i)) and count == 0:
        count += 1
        out_str.append(temp_string)
        temp_string = ''
for i in out_str:
    if not i[0].isupper():
        break_operation = 1
        break
if break_operation == 1:
    print('draft: ' + my_string[5:])
elif break_operation != 1:
    print('done. ' + my_string)
