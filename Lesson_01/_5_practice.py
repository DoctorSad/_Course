"""
    1. Создать переменные var_int, var_float, var_str,
        присвоив им 25, 4.5, 'python'
    2. Значение var_int увеличьте в 1.5 раза и присвойте переменной var_big
    3. Измените значение, хранимое в var_float уменьшив его на единицу
    4. Выведите на экран остаток от деления var_big на var_float
    5. Измените значение переменной var_str на 'end'
    6. Выведите значения всех переменных
"""

# 1
var_int = 25
var_float = 4.5
var_str = "python"

# вариант с множественным присваиванием
var_int, var_float, var_str = 25, 4.5, "python"

# 2
var_big = var_int * 1.5

# 3
var_float = var_float - 1

# с использованием оператора присваивания
# var_float -= 1

# 4
result = var_big % var_float
print(result)

# 5
var_str = "end"

# 6
print(var_big, var_float, var_str)
