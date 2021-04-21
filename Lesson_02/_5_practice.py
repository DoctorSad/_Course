# 1. Заполнить переменные a, b и с числами с помощью input()
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

# 2. Определить, сколько совпадающих значений переменных.
#   Вывести число: 3 (все совпадают), 2 (два совпадает) или 0 (все различны)
# if a == b and b == c:
if a == b == c:
    print(3)
elif a == b or a == c or b == c:
    print(2)
else:
    print(0)

# 3. Преобразовать переменные таким образом, чтоб
#   a = a + b
#   b = c - a
#   c = a + b + c
a, b, c = a + b, c - a, a + b + c

# 4. Вывести переменные a, b и c на экран.
print(a, b, c)

# 5. Для числа в переменной c вывести характеристики:
#   - отрицательное/положительное/ноль
#   - четное/нечетное

if c > 0:
    answer = "positive"
elif c < 0:
    answer = "negative"
else:
    answer = "zero"

answer = "positive" if c > 0 else "negative" if c < 0 else "zero"
print(answer)

if c % 2 == 0:
    print("even")
else:
    print("odd")

if c % 2:
    print("odd")
else:
    print("even")
