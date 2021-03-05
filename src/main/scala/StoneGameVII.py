class Solution:
    def stoneGameVII(self, stones):
        if not stones:
            return 0
        pref_sum = [0] * (len(stones) + 1)
        for i in range(len(stones)):
            pref_sum[i + 1] = pref_sum[i] + stones[i]

        n = len(stones)
        dp = [[0] * n for _ in range(n)]
        for l in range(2, n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n:
                    break
                sc1 = pref_sum[j+1] - pref_sum[i+1]
                sc2 = pref_sum[j] - pref_sum[i]

                dp[i][j] = max(sc1 - dp[i+1][j], sc2 - dp[i][j-1])
        return dp[0][n-1]



sol = Solution()
#print(sol.stoneGameVII([1]))
#print(sol.stoneGameVII([7,90,5,1,100,10,10,2]))#122
print(sol.stoneGameVII([5,3,1,4,2]))#6