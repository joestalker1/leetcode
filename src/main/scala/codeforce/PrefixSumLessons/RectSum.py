def solve():
    rows,cols = map(int, input().split())
    mat = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        mat.append(row)
    pr = [[0] * (cols + 1) for _ in range(rows + 1)]
    for i in range(rows):
        for j in range(cols):
            pr[i+1][j+1] = pr[i][j+1] + pr[i+1][j] - pr[i][j] + mat[i][j]
    q = int(input())
    for _ in range(q):
        lx,ly,rx,ry = list(map(int, input().split()))
        s = pr[rx][ry] - pr[lx-1][ry] - pr[rx][ly-1] + pr[lx-1][ly-1]
        print(s)


solve()