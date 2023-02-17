# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

cranes = input("How many cranes have been made: ")

try:
    cranes = int(cranes)
    petya_seryozha = cranes // 6
    katya = petya_seryozha * 4

    if petya_seryozha * 2 + katya == cranes:
        print(
            f"Petya made\t{petya_seryozha} cranes.\nKatya made\t{katya} cranes.\nSeryozha made\t{petya_seryozha} cranes.")
    else:
        print("It can't be.")
except ValueError:
    print("This is not an integer.")
except:
    print("Error.")
