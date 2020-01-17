class Solution:
    def change1(self, d, x):
        if not d or x <= 0:
            return 0
        mem = [[-1] * 10000 for _ in range(10)]

        def coin_change(i, s):
            if i < 0 or s < 0:
                return 100000000
            if s == 0:
                return 0
            if mem[i][s] != -1:
                return mem[i][s]
            res = 10000000
            res = min(res, coin_change(i - 1, s))
            res = min(res, 1 + coin_change(i, s - d[i]))
            mem[i][s] = res
            return res
        return coin_change(len(d) - 1, x)

    def change2(self, d, x):
        if not d or x <= 0:
            return 0
        huge = float('inf')
        dp = [[huge] * (1 + x) for _ in range(len(d))]
        for i in range(len(dp)):
            if d[i] < len(dp[0]):
                dp[i][d[i]] = 1

        for i in range(0, len(dp)):
            for s in range(1, len(dp[0])):
                if i >= 0:
                    dp[i][s] = min(dp[i][s],  dp[i-1][s])
                if 0 <= s - d[i] <= x:
                    dp[i][s] = min(dp[i][s], 1 + dp[i][s-d[i]])
        min_coins = dp[0][x]
        for i in range(1, len(dp)):
            min_coins = min(min_coins, dp[i][x])
        return min_coins


sol = Solution()
print(sol.change1([1, 2, 5, 10], 13))
print(sol.change2([1, 2, 5, 10], 13))