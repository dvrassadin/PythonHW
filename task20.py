# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.

# ноутбук
# 12

# string1 = "A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т"
# string2 = "D, G, Д, К, Л, М, П, У"
# string3 = "B, C, M, P, Б, Г, Ё, Ь, Я"
# string4 = "F, H, V, W, Y, Й, Ы"
# string5 = "K, Ж, З, Х, Ц, Ч"
# string8 = "J, X, Ш, Э, Ю"
# string10 = "Q, Z, Ф, Щ, Ъ"

# scores_table = {}

# for letter in string1.split(", "):
#     scores_table[letter] = 1
# for letter in string2.split(", "):
#     scores_table[letter] = 2
# for letter in string3.split(", "):
#     scores_table[letter] = 3
# for letter in string4.split(", "):
#     scores_table[letter] = 4
# for letter in string5.split(", "):
#     scores_table[letter] = 5
# for letter in string8.split(", "):
#     scores_table[letter] = 8
# for letter in string10.split(", "):
#     scores_table[letter] = 10

# print(scores_table)

scores_table = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1, 'А': 1,
                'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1, 'D': 2, 'G': 2, 'Д': 2,
                'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2, 'B': 3, 'C': 3, 'M': 3, 'P': 3, 'Б': 3, 'Г': 3,
                'Ё': 3, 'Ь': 3, 'Я': 3, 'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'Й': 4, 'Ы': 4, 'K': 5,
                'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5, 'J': 8, 'X': 8, 'Ш': 8, 'Э': 8, 'Ю': 8, 'Q': 10,
                'Z': 10, 'Ф': 10, 'Щ': 10, 'Ъ': 10}

word = input("Enter a word: ")
scores_count = 0

for letter in word:
    if letter in scores_table:
        scores_count += scores_table[letter]
    elif letter.swapcase() in scores_table:
        scores_count += scores_table[letter.swapcase()]
    else:
        print("The word contains incorrect characters.")
        break
else:
    print(f"You earned {scores_count} scores.")
