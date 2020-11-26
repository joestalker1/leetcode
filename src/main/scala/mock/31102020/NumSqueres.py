class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        dp = {}
        perf_num = []
        for i in range(1, int(n ** 0.5) + 1):
            a = i * i
            if a <= n:
                dp[a] = 1
                perf_num.append(a)
            else:
                break

        for s in range(1, n + 1):
            for j in range(len(perf_num) - 1, -1, -1):
                b = perf_num[j]
                if s - b < 0:
                    continue
                if (s - b) in dp:
                    if s in dp:
                        dp[s] = min(dp[s], dp[s - b] + 1)
                    else:
                        dp[s] = dp[s - b] + 1

        return dp[n]


sol = Solution()
print(sol.numSquares(40))
print(sol.numSquares(13))
print(sol.numSquares(12))
