class Solution:
    def longestLine(self, M):
        if not M or len(M[0]) == 0:
            return 0
        n = len(M)
        m = len(M[0])
        # hor,vert, diag, anti-diagonal
        # 3 dimensional array
        dp = [[[0] * 4 for _ in range(m)] for _ in range(n)]
        max_len = 0

        for i in range(n):
            for j in range(m):
                if M[i][j] == 1:
                    # define for horizontal
                    dp[i][j][0] = 1
                    if j > 0:
                        dp[i][j][0] = dp[i][j - 1][0] + 1
                    dp[i][j][1] = 1
                    if i > 0:
                        dp[i][j][1] = dp[i - 1][j][1] + 1
                    dp[i][j][2] = 1
                    if i > 0 and j > 0:
                        dp[i][j][2] = dp[i - 1][j - 1][2] + 1
                    dp[i][j][3] = 1
                    if i > 0 and j + 1 < m:
                        dp[i][j][3] = dp[i - 1][j + 1][3] + 1
                    # maximum among 4 values
                    max_len = max(max_len, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
        return max_len


arr = [[1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
       [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
       [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
       [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
       [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
       [1, 1, 0, 0, 1, 0, 1, 1, 1, 1],
       [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
       [1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
       [1, 1, 1, 1, 0, 0, 0, 1, 1, 0],
       [1, 1, 1, 0, 1, 1, 0, 1, 1, 1]]
sol = Solution()
print(sol.longestLine(arr))
