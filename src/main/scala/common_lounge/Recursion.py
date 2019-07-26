def f(x, y):
    if y == 0:
        return 1
    a = f(x, y // 2)
    if y % 2 == 0:
        return a * a
    else:
        return a * a * x

def f1(x, y):
    if y == 0:
        return 1
    if y == 1:
        return x
    a = f1(x, y // 2)
    if y % 2 == 0:
        return f1(x, y // 2) * f1(x, y // 2)
    else:
        return f1(x, y // 2) * f1(x, y // 2) * x


print(f1(2, 5))


