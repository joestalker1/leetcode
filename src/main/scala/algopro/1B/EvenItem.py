def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    for a in arr:
        if a % 2 == 0:
            print(a,end=' ')

solve()