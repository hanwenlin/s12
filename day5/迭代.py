def func(n):
    n += 1
    if n >= 4:
        return 'end'
    print(n)
    return func(n)

r = func(1)
print(r)