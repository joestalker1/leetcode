class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return 0
        pr = [0] * len(stones)
        pr[0] = stones[0]
        for i in range(1, len(stones)):
            pr[i] = pr[i - 1] + stones[i]

        dp = [0] * len(stones)
        dp[-1] = pr[-1]
        # consider if alice takse n stones or n-1 stones and bob takes n stones.
        # in first case the difference is sum[n] and at second case is sum[n-1] - diff[n]
        # we consider the score - difference, but here we have either sum[n] - 0 or sum[n-1] - diff[n]
        for i in range(len(stones) - 2, -1, -1):
            dp[i] = max(dp[i + 1], pr[i] - dp[i + 1])
        return dp[1]
