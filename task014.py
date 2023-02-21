# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

number = int(input("Enter an integer: "))
pow = 1

while pow <= number:
    print(pow, end=", ")
    pow *= 2
