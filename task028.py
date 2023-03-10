# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# 2 2
#     4

def sum_rec(a, b):
    return a if b == 0 else sum_rec(a + 1, b - 1)


print(sum_rec(50, 3))
