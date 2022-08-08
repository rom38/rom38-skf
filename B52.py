# %%
# 5.2.3
L = ['a', 'b', 'c']
print(id(L))

L.append('d')
print(id(L))
# %%
# 5.2.4
a = 5
b = 3+2
print(id(a),id(b))
id(a)-id(b)

# %%
# 5.2.5
a = 0
b = 0

while id(a) == id(b):
    a += 1
    b += 1

print(a)

# %%
# 5.2.7

a = 0
b = 0

while id(a) == id(b):
    a -= 1
    b -= 1

print(a)


# %%
# 5.2.8

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30",
 ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])
print( id(list_id_before), id(list_id_after))


print( list_id_before == list_id_after )
# %%
# 5.2.9

text = input("Введите текст:")

unique = set(text)

print("Количество уникальных символов: ", len(unique))

# %%
# 5.2.10

text = "The Zen of Python"

unique = set(text)

print("Количество уникальных символов: ", len(unique))
# %%
abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debtors = abons.difference(debtors)

print(non_debtors)
# {'Васильев', 'Иванов'}
# %%
# 5.2.11

#a = input("Введите первую строку: ")
#b = input("Введите вторую строку: ")

a = "Введите первую строку: "
b = "Введите вторую строку: "

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)

print(a_and_b)
# %%
# 5.2.12

a = "1 2 3 4 5 6 7 8".split()
b = "2 4 6 8 10 12".split()
a_set, b_set = set(a), set(b) # используем множественное присваивание
a_and_b = a_set.symmetric_difference(b_set)
print(a_and_b)

# %%
