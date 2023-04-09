def solve():
    x,y,z = map(float, input().split())
    n = int(input())
    X = 0
    Y = 0
    Z = 0
    eps = 1e-7
    for _ in range(n):
        a,b,c,q = map(float, input().split())
        if abs(q - 0.0) < eps:
            continue
        X += a * q
        Y += b * q
        Z += c * q
    if X >= x - eps and Y >= y - eps and Z >= z - eps:
        print('YES')
    else:
        print('NO')


solve()

