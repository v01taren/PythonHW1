# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

numbers, sum = int(input("Введите трехзначное число:")), 0
while numbers:
    sum, numbers = sum + numbers % 10, numbers // 10
print(sum)
