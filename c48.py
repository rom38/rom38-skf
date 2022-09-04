# %%

import random  # модуль, с помощью которого перемешиваем массив

# пусть имеем массив всего лишь из 9 элементов
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

is_sort = False  # станет True, если отсортирован
count = 0  # счетчик количества перестановок

while not is_sort:  # пока не отсортирован
    count += 1  # прибавляем 1 к счетчику

    random.shuffle(array)  # перемешиваем массив

    # проверяем отсортирован ли
    is_sort = True
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            is_sort = False
            break

print(array)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(count)
# 290698
# %%
n = 1
for i in range(1, 101):
    n *= i
s = str(n)
print(len(s))
print(n)

# %%


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i, ar_el in enumerate(array):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i + 1, len(array)):
        count += 1
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]

print(array)
print(count)

# %%


array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
count = 0
for i, ar_el in enumerate(array):  # проходим по всему массиву
    idx_max = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i + 1, len(array)):
        count += 1
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)
print(count)

# %%

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(len(array)):
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print(array)

# %%

# for j = 2 to A.length do
#     key = A[j]
#     i = j-1
#     while (int i > 0 and A[i] > key) do
#         A[i + 1] = A[i]
#         i = i - 1
#     end while
#     A[i+1] = key
# end [5]
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(array)
count = 0
len_ar = len(array)
for j in range(1, len_ar):  # проходим по всему массиву
    key_el = array[j]
    i = j - 1
    while i >= 0 and array[i] > key_el:
        count += 1
        array[i+1] = array[i]
        i -= 1

    count += 1
    array[i+1] = key_el

print(array)
print(count)

# %%

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
print(array)
def merge_sort(L):  # «разделяй»
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # «властвуй»
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(array))
print(count)

# %%

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]


def qsort_random(array, left=0, right=len(array)-1):
    p = random.choice(array[left:right+1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            # count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)
    return array


print(qsort_random(array))

# %%
