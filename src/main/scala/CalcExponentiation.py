def power(x, y):
    res = x
    if y < 0:
        y = -y
    #stash odd number of power
    c = 1
    while y > 1:
        if y % 2 == 0:
            res *= res
            y = y // 2
        else:
            c *= res
            res *= res
            y = (y - 1)//2
    return c * res


print(power(2, 15))
print(2 ** 15)