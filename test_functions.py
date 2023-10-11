def lamb(n):
    return lambda a: a * n


ret = lamb(4)

print(ret(10))
