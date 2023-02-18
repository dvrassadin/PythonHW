# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("Enter an three-digit integer: ")

try:
    number = int(number)
    sum = 0

    if number < 0:
        number = -number

    sum += number % 10
    number //= 10
    sum += number % 10
    number //= 10
    sum += number % 10

    print(f"Sum is {sum}.")
except ValueError:
    print("This is not an integer.")
except:
    print("Error.")
