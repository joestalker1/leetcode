def solve():
    n,m = map(int, input().split())
    arr = [[1] * m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            arr[i][j] = arr[i-1][j] + arr[i][j-1]
    for i in range(n):
        print(*arr[i])


solve()


