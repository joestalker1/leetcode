def solve():
    a = float(input())
    b = float(input())
    c = float(input())
    eps = 1e-12
    if abs(a + b - c) < eps:
        print('yes')
    else:
        print('no')


solve()
