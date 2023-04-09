def solve():
    a = int(input())
    b = int(input())
    return [c for c in range(a,b+1) if c % 2 == 0]


print(' '.join(map(str, solve()) ))