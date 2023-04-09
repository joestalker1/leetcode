
def find_prefix_sum(diffs):
    n = len(diffs)
    m = len(diffs[0])
    pre = [[0] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            pre[i+1][j+1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + diffs[i][j]
    return pre


def solve():
    rows,cols = list(map(int,input().split()))
    arr = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        arr.append(row)
    q = int(input())
    diffs = [[0] * cols for _ in range(rows)]
    for _ in range(q):
        lx,ly,rx,ry,d = list(map(int, input().split()))
        lx -= 1
        ly -= 1
        diffs[lx][ly] += d
        if ry < cols:
            diffs[lx][ry] -= d
        if rx < rows:
            diffs[rx][ly] -= d
        if rx < rows and ry < cols:
            diffs[rx][ry] += d
    pre = find_prefix_sum(diffs)
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = pre[i+1][j+1] + arr[i][j]
    for row in arr:
        print(' '.join(map(str,row)))


solve()

