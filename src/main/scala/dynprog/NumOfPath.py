def numOfPath(m, n):
    cache = [0] * m
    for i in range(m):
        cache[i] = [0] * n
    for i in range(m):
        cache[i][0] = 1
    for j in range(n):
        cache[0][j] = 1
    for i in range(m):
        for j in range(n):
            cache[i][j] = cache[i-1][j] + cache[i][j - 1]
    return cache[m - 1][n - 1]


def can_go(xy, arr):
    if not arr or len(arr) == 0:
        return True
    x = xy[0]
    y = xy[1]
    for i in range(0, len(arr), 2):
        x1 = arr[i][0]
        y1 = arr[i][1]
        x2 = arr[i+1][0]
        y2 = arr[i+1][1]
        if x1 == x2:
            if y1 <= y <= y2:
                return False
        elif x1 <= x <= x2:
            return False
    return True


def numOfRoad(m, xy, forbid_path = []):
    if m == 0:
        return 0
    x = xy[0]
    y = xy[1]
    grid = [0] * m
    for i in range(m):
        grid[i] = [0] * m
    for i in range(0, m - 1):
        grid[i][0] = 1
    for i in range(1, m):
        grid[m-1][i] = 1
    for i in range(m - 2, y - 1, -1):#row
        for j in range(1, x + 1):#column
            if can_go([i,j], forbid_path):
                a = grid[i+1][j] if can_go([i+1,j], forbid_path) else 0
                b = grid[i][j-1] if can_go([i, j - 1], forbid_path) else 0
                c = grid[i+1][j-1] if can_go([i+1,j-1], forbid_path) else 0
                grid[i][j] = a + b + c

    return grid[y][x]

print("%s" % numOfRoad(4, [3, 0]))



