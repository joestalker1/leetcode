def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    pr = [0] * (n+1)
    for i in range(1, len(pr)):
        pr[i] = pr[i-1] + arr[i-1]
    print(*pr)


solve()