def unboundedKnapsack(W, val, wt):
    dp = [0] * (W + 1)
    for w in range(W + 1):
        for j in range(len(val)):
            if wt[j] <= w:
                dp[w] = max(dp[w], dp[w - wt[j]] + val[j])
    return dp[-1]

print(unboundedKnapsack(100, [1,30], [1, 50]))

