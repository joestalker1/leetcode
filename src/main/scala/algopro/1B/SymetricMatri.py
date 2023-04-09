def solve():
    n = int(input())
    arr = []
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    for i in range(1, n):
        for j in range(n):
            if i == j:
                break
            if arr[i][j] != arr[j][i]:
                print('no')
                return
    print('yes')


solve()