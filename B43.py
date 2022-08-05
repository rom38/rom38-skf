
# %%
# 4.3.4
def rec_reverce(str_1):
                                                                                            ...:    if not str_1:                                                                                                             ...:        return ''                                                                                                             ...:    return rec_reverce(str_1[1:])+str_1[0]                                                                                    ...:                                                                                                                              ...: rec_reverce('give')  # 55
# %%
# 4.3.5
def sum_digit(n):
    if n < 10:
       return n
    else:
       return n % 10 + sum_digit(n // 10)


sum_digit(123)  # 6
# %%
