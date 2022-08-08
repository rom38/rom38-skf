# %%
from tkinter import N


def linear_solve(a, b):
    if a: 
        return b / a
    elif not a and not b: # снова используем числа в логических выражениях
        return "Бесконечное количество корней"
    else:
        return "Нет корней"
        
linear_solve(0,0)
# %%
# 5.4.3
def descrem_f(a,b,c):
    descrem = b**2 - 4*a*c
    return descrem

descrem_f(7,8,9)


# %%
# 5.4.4
def quadratic_solve(a, b, c):
    if descrem_f(a,b,c) < 0:
        print("Нет вещественных корней")
quadratic_solve(7,8,9)

# %%
# 5.4.5
def quadratic_solve_2(a, b, c):
    if descrem_f(a,b,c) < 0:
        print("Нет вещественных корней")
        return "Нет вещественных корней"

    elif descrem_f(a,b,c)==0:
        root_1 = -b/(2*a)
        print(f"Уравнение имеет один корень: {root_1}")
        return root_1
    else:
        return (-b - descrem_f(a,b,c) ** 0.5) / (2 * a),\
            (-b + descrem_f(a, b, c) ** 0.5) / (2 * a)

quadratic_solve_2(1,20,1)

# %%
L=[10,20,7]
print(*L)
print (quadratic_solve_2(*L))
# %%

# %%
# 5.4.9

def min_el (LL:list):
    if len(LL) == 1:
        return LL[0]
    if len(LL) == 2:
        a, b = LL[0],LL[1]
        if a<=b:
            return a
        else:
            return b
    min_rec=min_el(LL[1:])
    if LL[0]<=min_rec:
        return LL[0]
    else:
        return min_rec

min_el ([1,2,3,-1,-8,-2])


# %%
# 5.4.10
def rev_digit(n, res=0):
    print (res)
    if n < 10:
       return n
    else:
       return rev_digit(n // 10, res+1) + (n % 10)*10**res

rev_digit(13788)
# %%
def mirror(a, res=0):
    print (a,res)
    return mirror(a // 10, res*10 + a % 10) if a else res 
mirror(871)
# %%

def equal(N, S):
    if S < 0:
        return False
    if N < 10:
        return N == S
    else:
        return equal(N // 10, S - N % 10) 
equal(678,21)

# %%
# 5.4.13
def ee():
    n=0
    while True:
        n+=1
        print(n)
        yield (1+1/n)**n 

last = 0
for a in ee(): # e() - генератор
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break # после достижения которого - завершаем цикл
    else:
        last = a # иначе - присваиваем новое значение 
# %%
# 5.4.14
iter_obj = iter("Hello!")

print(next(iter_obj)) 
print(next(iter_obj)) 
print(next(iter_obj)) 
print(next(iter_obj)) 
print(next(iter_obj)) 
print(next(iter_obj)) 
print(next(iter_obj)) 
print(next(iter_obj)) 
# %%
