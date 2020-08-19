class Solution(object):
    def knightProbability(self, N, K, r, c):
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        for _ in range(K):
            #allocate new array
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            # calculate probality to be at [r+dr][c+dc]
                            # we may put here many times,so there are mutually exclusive so sum up their probalities
                            dp2[r+dr][c+dc] += val / 8.0
            # make new one as current
            dp = dp2

        return sum(map(sum, dp))



sol = Solution()
print(sol.knightProbability(8, 30, 6, 4))
print(sol.knightProbability(3, 2, 0, 0))
