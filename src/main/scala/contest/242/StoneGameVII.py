class Solution:
    def stoneGameVII(self, stones):
        if not stones:
            return 0
        pref_sum = [0] * (len(stones) + 1)
        for i in range(len(stones)):
            pref_sum[i + 1] = pref_sum[i] + stones[i]
        n = len(stones)
        dp = [[-1] * n for _ in range(n)]

        def play(alice, l, r, dp):
            if l == r:
                return 0

            if dp[l][r] != -1:
                return dp[l][r]

            sc1 = pref_sum[r + 1] - pref_sum[l + 1]
            sc2 = pref_sum[r] - pref_sum[l]
            if alice:
                d = max(sc1 + play(False, l + 1, r, dp), sc2 + play(False, l, r - 1, dp))
            else:
                d = min(play(True, l + 1, r, dp) - sc1, play(True, l, r - 1, dp) - sc2)
            dp[l][r] = d
            return d

        pr = play(True, 0, len(stones) - 1, dp)
        return pr


sol = Solution()
print(sol.stoneGameVII([5,3,1,4,2]))
