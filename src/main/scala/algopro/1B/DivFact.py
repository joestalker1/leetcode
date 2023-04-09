import math

def solve():
    n = int(input())
    res = 1
    eps = 1e-12
    fact = 1
    for i in range(1, n+1):
        fact *= i
        res += 1 / fact
        if abs(res - math.exp(1)) < eps:
            break
    print(res-eps)


solve()
