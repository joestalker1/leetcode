def solve():
    n,m = map(int, input().split())
    arr = []
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
    row = 0
    col = 0
    max_val = arr[row][col]
    for i in range(n):
        for j in range(m):
            if arr[i][j] > max_val:
                max_val = arr[i][j]
                row = i
                col = j
    print(max_val)
    print('{} {}'.format(row, col))


solve()