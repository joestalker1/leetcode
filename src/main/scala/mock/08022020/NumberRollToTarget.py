class Solution:
    def numRollsToTarget(self, d, f, target):
        dp = [[0] * (target+1) for _ in range(d+1)]
        for i in range(1, target+1):
            if i <= f:
                dp[1][i] = 1
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                fc = 1
                while fc < j and fc <= f:
                    dp[i][j] += dp[i-1][j-fc]
                    fc += 1
        return dp[d][target]

sol = Solution()
print(sol.numRollsToTarget(d = 2, f = 6, target = 7))
print(sol.numRollsToTarget(d = 1, f = 6, target = 3))

