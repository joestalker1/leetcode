class Solution:
    def numRollsToTarget(self, d, f, target):
        dp = [[0] * d for _ in range(target + 1)]
        # set way to roll sum with one die is 1
        for i in range(1, min(f, target) + 1):
            dp[i][0] = 1

        for sums in range(1, target + 1):
            for dice in range(1, d):
                for k in range(1, min(f, sums) + 1):
                    dp[sums][dice] += dp[sums - k][dice-1]
        return dp[target][-1] % (10 ** 9 + 7)


sol = Solution()
print(sol.numRollsToTarget(d = 2, f = 6, target = 7))
#print(sol.numRollsToTarget(d = 30, f = 30, target = 500))
#print(sol.numRollsToTarget(d = 1, f = 6, target = 3))
