class Solution:
    def lastStoneWeightII(self, stones):
        if not stones:
            return 0

        dp = [float('inf')] * (len(stones) + 1)
        dp[0] = 0
        for i in range(1, len(stones) + 1):
            x = -stones[i - 1] + dp[i - 1]
            y = 
            dp[i] = min(abs(-stones[i - 1] + dp[i - 1], stones[i - 1] + dp[i - 1])
        return min([abs(x) for x in dp[1:]])


sol = Solution()
# print(sol.lastStoneWeightII([2, 2]))
print(sol.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
