from re import A
from tkinter.messagebox import YES


# %%
def fib():
    a, b = 0, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

# %%
for ii, num in enumerate(fib()):
    print (num)
    if ii == 10:
        break


# %%
iter_fib= iter(fib())
print(next(iter_fib))
print(next(iter_fib))

# %%
# 4.4.1

def naturo(base=10, step=2):
    yield base
    
    while True:
        base +=  step
        yield base

for ii, num in enumerate(naturo()):
    print (num)
    if ii == 10:
        break
# %%
# 4.4.2

def liist(ll=None):
    if not ll:
        ll=[]
 
    while True:
        for ii in ll:
            yield ii
                
        

for ii, num in enumerate(liist([1,2,3])):
    print (num)
    if ii == 10:
        break
# %%
