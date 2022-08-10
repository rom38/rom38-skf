# %%
# 5.5.1
import string
L = ['THIS', 'IS', 'LOWER', 'STRING']
p = "KKK".lower()
print(list(map(str.lower, L)))

# %%
# Из заданного списка вывести только положительные элементы


def positive(x):
    return x > 0  # функция возвращает только True или False


result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])

# Возвращается итератор, т.е. перечисляйте или приводите к списку
print(list(result))   # [1, 2]

# %%
# 5.5.2


def even(x):
    return x % 2 == 0


result = filter(even, [-2, -1, 0, 1, -3, 2, -3])

print(list(result))   # [-2, 0, 2]
# %%
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive_2(x): return x > 0


print(some_list)
print(list(map(pow2, filter(positive_2, some_list))))
# %%
some_list = [i - 10 for i in range(20)]
[i**2 for i in some_list if i > 0]
# %%

# Возвести первые 10 натуральных чисел в квадрат
list(map(lambda x: x ** 2, range(1, 11)))  # правильно
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# неправильно, так как lambda содержит две конструкции
list(map(lambda x: x ** 2, range(1, 11)))
# %%
d = {2: "c", 1: "d", 4: "a", 3: "b"}

# Чтобы отсортировать его по ключам нужно сделать так
print(dict(sorted(d.items())))
# {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
# %%
sorted(d.items(), key=lambda x: x[1])  # сортировка по значению словаря
# %%
# d.items()[1]
# %%
# 5.5.3

# (вес, рост)
data = [
    (82, 1.91),
    (68, 1.74),
    (90, 1.89),
    (73, 1.79),
    (76, 1.84)
]

data_imt = list(map(lambda x: x[0]/x[1]**2, data))
filter_imt = filter(lambda x: x < 22.7, data_imt)
list(filter_imt)
# %%

# (вес, рост)
data = [
    (82, 1.91),
    (68, 1.74),
    (90, 1.89),
    (73, 1.79),
    (76, 1.84)
]
list(sorted(data, key=lambda x: x[0]/x[1]**2))
#list(filter(lambda x: x<22.7,[i/j**2 for i,j in data]))

# %%
# 5.5.4
print(min(data, key=lambda x: x[0]/x[1]**2))

# %%
# 5.5.5

a = ["asd", "bbd", "ddfa", "mcsa"]

print(list(map(len, a)))
# %%
# 5.5.6
a = ["это", "маленький", "текст", "обидно"]

print(list(map(str.upper, a)))
# %%
