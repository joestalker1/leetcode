class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6
        MOD = 10 ** 9 + 7
        dp0 = [[0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0],
               [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0]]
        dp1 = [[0] * 6 for _ in range(6)]
        for i in range(3, n + 1):
            # d is new side
            for d in range(0, 6):
                # p is previous side
                for p in range(0, 6):
                    dp1[d][p] = 0
                    if dp0[d][p]:
                        # pp is previous of p
                        for pp in range(6):
                            if pp == d:
                                continue
                            dp1[d][p] = (dp1[d][p] + dp0[p][pp]) % MOD

            dp0, dp1 = dp1, dp0
            # dp0 has resulting sum
        cnt = 0
        for i in range(6):
            cnt = (cnt + sum(dp0[i])) % MOD
        return cnt