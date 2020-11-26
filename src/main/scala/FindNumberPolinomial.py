def findPolyNumber(s, i1,i2):
    if not s:
        return 0
    n = len(s)
    pol = [[0] * n for _ in range(n)]
    for ln in range(1, n+1):
        for i in range(n - ln +1):
            j = i + ln - 1
            if ln == 1:
                pol[i][j] = 1
            elif ln == 2:
                if s[i] == s[j]:
                    pol[i][j] = 1
            else:
                if s[i] == s[j] and pol[i+1][j-1] == 1:
                    pol[i][j] = 1

    dp = [[0] * n for _ in range(n)]
    for ln in range(1, n + 1):
        for i in range(n - ln + 1):
            j = i + ln - 1
            dp[i][j] = pol[i][j]
            for k in range(i, j):
                dp[i][j] += pol[i][k] * dp[k+1][j]
    return dp[i1][i2]
print(findPolyNumber('messeye', 0, 6))
print(findPolyNumber('messeye', 1, 4))
