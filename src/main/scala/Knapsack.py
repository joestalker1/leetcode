def knapsack(W, val, wt):
    n = len(val)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(n + 1):#try every i in line
        for w in range(W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w - wt[i - 1]] + val[i - 1], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]


print(knapsack(50, [60, 100, 120], [10, 20, 30]))
