# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint

list_length = int(input("Enter the length of the list: "))

list = [randint(1, 100) for _ in range(list_length)]

print(list)

number_to_find = int(input("Enter an integer to find: "))

dictionary = {}

for number in list:
    dictionary[number] = dictionary.get(number, 0) + 1

if number_to_find in dictionary:
    print(
        f"The number {number_to_find} appears in the list {dictionary[number_to_find]} times.")
else:
    print(f"There isn't number {number_to_find} in the list.")
    close_index = None  # The index of the bigger close value
    sorted_list = sorted(list)

    for i in range(list_length):
        if sorted_list[i] > number_to_find:
            close_index = i
            break

    if number_to_find - sorted_list[close_index - 1] < sorted_list[close_index] - number_to_find:
        print(f"The closest value is {sorted_list[close_index - 1]}.")
    else:
        print(f"The closest value is {sorted_list[close_index]}.")
