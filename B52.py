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
