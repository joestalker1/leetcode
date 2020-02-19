class Solution:
    def uniquePaths(self, m: int, n: int):
        #m is column number
        dp = [[0] * m for _ in range(n)]
        for i in range(m):
            dp[0][i] = 1
        for i in range(n):
            dp[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
        return dp[-1][-1]


sol = Solution()
print(sol.uniquePaths(m = 7, n = 3))
print(sol.uniquePaths(m = 3, n = 2))