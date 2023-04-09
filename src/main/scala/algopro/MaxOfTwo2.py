def solve():
    n1 = int(input())
    n2 = int(input())
    if n1 == n2:
        return 0
    if n1 > n2:
        return 1
    return 2


print(solve())