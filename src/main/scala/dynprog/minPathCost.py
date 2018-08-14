def minPathCost(cost, m, n):
    mem = [0] * (m + 1)
    for i in range(m+1):
        mem[i] = [0] * (n+1)
    mem[0][0] = cost[0][0]
    for j in range(1, n):
        mem[0][j] = mem[0][j-1] + cost[0][j]
    for i in range(1, m):
        mem[i][0] = mem[i-1][0] + cost[i][0]
    for i in range(1, m):
        for j in range(1, n):
            x = mem[i-1][j]
            y = mem[i][j - 1]
            z = mem[i-1][j-1]
            mem[i][j] = min(x, y, z) + cost[i][j]
    return mem[m-1][n-1]

cost = [[1,2,3],
        [1,1,1],
        [2,4,1]]
print(minPathCost(cost, 3, 3))