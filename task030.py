# Задача 30: Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

first_number = int(input("First number: "))
step = int(input("Step: "))
size = int(input("List size: "))

numbers = [i for i in range(first_number, size * step + first_number, step)]

print(numbers)
