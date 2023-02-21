# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

sum = int(input("Enter a sum: "))
product = int(input("Enter a product: "))
was_found = False
i = 1
j = 1

while (i <= product or i < sum) and not was_found:
    while (j <= product or j < sum) and not was_found:
        current_product = i * j
        if current_product > product:
            break
        elif current_product == product:
            if i + j == sum:
                print(f"Numbers are {i} and {j}.")
                was_found = True
        j += 1
    j = 1
    i += 1
if not was_found:
    print("There are no suitable numbers.")
