def knapsack(c, weight, val, n):
    table = [0] * (n + 1)
    for i in range(0, n + 1):
        table[i] = [0] * (c + 1)

    for i in range(1, n + 1):
        for cp in range(1,c + 1):
            if weight[i-1] <= cp:
                x = cp - weight[i - 1]
                table[i][cp] = max(val[i-1] + table[i-1][x], table[i-1][cp])
            else:
                table[i][cp] = table[i-1][cp]
    return table[n][c]


print(knapsack(5,[2,3,4,5],[3,4,5,6], 4))


