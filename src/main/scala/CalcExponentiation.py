def power(x, y):
    base = x
    exp = y
    if y < 0:
        exp = -exp
    c = 1
    while exp > 1:
        print("bu!")
        if exp % 2 == 0:
            base *= base
            exp = exp // 2
        else:
            c *= base
            base *= base
            exp = (exp - 1)//2
    return c * base


print(power(2, 15))
print(2 ** 15)