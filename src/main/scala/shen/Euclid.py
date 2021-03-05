def diofantEquation(a, b):
    #m = p * a + q * b; n = r * a + s * b. nod (a,b) = nod (m,n); m,n >= 0
    m = a
    n = b
    p = 1
    q = 0
    r = 0
    s = 1
    while m != 0 and n != 0:
        if m >= n:
            m = m - n
            p = p - r
            q = q - s
        else:
            n = n - m
            r = r - p
            s = s - q
    if m == 0:
        k = n
        x = r
        y = s
    else:
        k = m
        x = p
        y = q
    return [k,x,y]

print(diofantEquation(30, 40))