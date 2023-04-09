def solve():
    a = int(input())
    if a == 0:
        return 0
    if a > 0:
        return 1
    return -1

print(solve())