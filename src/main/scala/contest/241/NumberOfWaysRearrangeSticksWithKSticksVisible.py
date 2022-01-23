class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        # assert self._rearrangeSticks(2:2) == 1,'n == k'
        # assert self._rearrangeSticks(3, 2) == 2,'n > k'
        # assert self._rearrangeSticks(1, 0) == 1,'k == 0'
        return self._rearrangeSticks(n, k)

    def _rearrangeSticks(self, n: int, k: int) -> int:
        if n < k:
            return 0
        MOD = 10 ** 9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][1] = 1
        for i in range(2, n + 1):
            for j in range(1, k + 1):  # sticks
                dp[i][j] = (dp[i - 1][j - 1] % MOD + ((i - 1) * dp[i - 1][j]) % MOD) % MOD
        return dp[n][k]
