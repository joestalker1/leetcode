def longPoliSub(s):
    if not s or len(s) == 0:
        return 0
    n = len(s)
    dp = [[0] *(n+1) for _ in range(n+1)]
    for i in range(len(s)+1):
        dp[i][i] = 1

    for k in range(2, n + 1):
        for i in range(0, n - k + 1):
            j = i + k - 1
            if s[i] == s[j] and k == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
    return dp[0][n - 1]

print(longPoliSub("BBABCBCAB"))
