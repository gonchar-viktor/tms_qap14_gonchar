# +++
# 1. Создайте словарь, связав его с переменной school, и наполните его данными, +
# которые бы отражали количество учащихся в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {"1a": 20, "2a": 21, "3a": 22, "4a": 23, "5a": 24, "1б": 25, "2б": 26, "3б": 27, "4б": 28, "5б": 29}

# 2. Узнайте сколько человек в каком-нибудь классе. +
a = school["2a"]
print(a)

# 3. Представьте, что в школе произошли изменения, внесите их в словарь: +
# ◦ в трех классах изменилось количество учащихся;
# ◦ в школе появилось два новых класса;
# ◦ в школе расформировали один из классов.
school["1a"] = 19
school["2a"] = 20
school["3a"] = 21
# 3.1
school["1в"] = 30
school["2в"] = 31
# 3.2
del school["5б"]
# 3.3

# 4. Выведите содержимое словаря на экран. +
print(school)

