# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

from random import randint

number_of_coins = int(input("Number of coins: "))
number_of_one, number_of_zero = 0, 0

for i in range(number_of_coins):
    coin = randint(0, 1)
    print(coin, end=" ")
    if coin == 1:
        number_of_one += 1
    elif coin == 0:
        number_of_zero += 1

print(
    f"\nMinimum number of coins to flip is {min(number_of_one, number_of_zero)}.")
