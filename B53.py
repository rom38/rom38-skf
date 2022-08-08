# %%
# 5.3.2
some_var = 1
some_var = None
some_var = (2,)
if some_var is None:
    print("NoneType")
else:
    print(type(some_var))
# %%
# 5.3.3
a = None # пустая строка
b = a or 1
print(b)

# %%
# 5.3.4

a = "foo"
b = "bar"

print(1 and a or b)
# %%
# 5.3.5
a = ""
b = "bar"

print(1 and a or b)
# %%
