def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    pr = [0] * (n + 1)
    for i in range(n):
        pr[i + 1] = pr[i] ^ arr[i]
    m = int(input())
    for _ in range(m):
        l,r = list(map(int, input().split()))
        print(pr[r] ^ pr[l-1])


solve()