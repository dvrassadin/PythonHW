# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

try:
    length = int(input("Chocolate bar length: "))
    width = int(input("Chocolate bar width: "))
    pieces = int(input("How many pieces do you want: "))

    print("Yes!") if pieces % width == 0 or pieces % length == 0 else print("No.")
except ValueError:
    print("This is not an integer.")
except:
    print("Error.")
