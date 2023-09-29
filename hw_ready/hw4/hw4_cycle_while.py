# +++
# 1. Дано число N. Найти произведение всех чисел от 0 до N. +
N = 7
i = 0
o = 1
while i < N:
    i += 1
    o *= i

print(o)

# 2. Поле засеяли цветами двух сортов на площади S1 и S2. Каждый год +
# площадь цветов первого сорта увеличивается вдвое, а площадь второго сорта
# увеличивается втрое. Через сколько лет площадь первых сортов будет
# составлять меньше 10% от площади вторых сортов.
# ---  Процент от числа = (число * процент) / 100
s1 = int(input("Введите S1: "))
s2 = int(input("Введите S2: "))
year = 0
s3 = (s2 * 10) / 100   # 10% от S2
while s1 > s3:
    s1 = s1 * 2
    s2 = s2 * 3
    s3 = (s2 * 10) / 100
    year += 1

print(year)

# 3. Дано целое число N (>0). Используя операции деления нацело и взятия +
# остатка от деления, найти количество и сумму его цифр.
N = int(input("Введите целое число которое больше нуля: "))
if N <= 0:
    print("Error: число не подходит, повторите попытку!")
summ_result = 0
kolvo_result = 0
h = 0
while N > 0:
    if N > 0:
        h = N % 10
        kolvo_result += 1
        summ_result += h
        N = N // 10

print("кол-во чисел:", kolvo_result)
print("сумма чисел:", summ_result)

# # 4. Деду M лет, а внуку N лет. Через сколько лет дед станет вдвое старше +
# # внука. И сколько при этом лет будет деду и внуку
# # ded_M = 78
# # vnuk_N = 38
ded_M = int(input("Введите сколько лет деду: "))
vnuk_N = int(input("Введите сколько лет внуку: "))
year = 0
while ded_M / vnuk_N != 2:
    ded_M += 1
    vnuk_N += 1
    year += 1

print(year)

