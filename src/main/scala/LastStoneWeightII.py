class Solution:
    def lastStoneWeightII(self, stones):
        if not stones:
            return 0
        n = sum(stones)
        S2 = 0
        S = sum(stones)
        n = len(stones)
        dp = [[0] * (S + 1) for _ in range(n + 1)]
        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for s in range(1, S// 2 + 1):
                if dp[i - 1][s] > 0 or s >= stones[i-1] and dp[i-1][s-stones[i-1]] > 0:
                    dp[i][s] = 1
                    S2 = max(S2, s)
        return S - 2 * S2


sol = Solution()
# print(sol.lastStoneWeightII([3,1,2]))
print(sol.lastStoneWeightII([2, 7, 4, 1, 8, 1]))
