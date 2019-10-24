def exspenses(m, d, i, v):
    for _ in range(m):
        v = (1 + i) * v - d
    return v

def calc(m, v, i):
    lo = 1
    hi = v * (1 + i)
    e = 10 ** (-9)
    while lo < hi:
        d = lo + (hi - lo) / 2
        b = exspenses(m, d, i, v)
        if abs(hi - lo) <= e:
            return d
        elif b > 0:#undershoot
            lo = d + 1
        else:
            hi = d - 1
    return lo

print(calc(2, 1000, 0.1))




