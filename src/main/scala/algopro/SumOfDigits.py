def solve():
    n = int(input())
    d0 = n % 10
    d1 = (n // 10) % 10
    d2 = (n // 100) % 10
    return d0 + d1 + d2

print(solve())