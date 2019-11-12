def edit_distance(s1, s2):
    if not s1 and not s2:
        return 0
    m = len(s1)
    n = len(s2)
    # s1 to s2
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
    return dp[m][n]




