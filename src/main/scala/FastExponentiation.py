def pow(x, p):
    res = 1
    while p:
        if p & 1 == 1:
            res = res * x
        x *= x
        p = p // 2
    return res

def pow2(x, p):
    print('{}'.format(1))
    if p == 1:
        return x
    if p & 1 == 1:
        n = (p - 1)//2
        res = pow2(x, n)
        return res * res * x
    res = pow2(x, p // 2)
    return res * res

print(pow2(2, 16))
