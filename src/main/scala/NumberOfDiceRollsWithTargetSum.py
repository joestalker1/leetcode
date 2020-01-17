class Solution:
    def numRollsToTarget(self, d, f, target):
        if not d or not target or not f:
            return 0
        dp = [[0] * (target + 1) for i in range(d)]
        for j in range(target+1):
            for i in range(d):
                if i == 0:
                    if 0 < j <= f:
                        dp[i][j] = 1
                else:
                    ways = 0
                    for k in range(1, min(j, f + 1)):
                        ways += dp[i-1][j-k]
                    dp[i][j] = ways
        return dp[d-1][target] % (10 ** 9 + 7)


sol = Solution()
print(sol.numRollsToTarget(d = 2, f = 5, target = 10))#1
print(sol.numRollsToTarget(d = 30, f = 30, target = 500))
print(sol.numRollsToTarget(d = 2, f = 6, target = 7))
print(sol.numRollsToTarget(d = 1, f = 6, target = 3))