class Solution:
    def findMaxForm(self, strs, m: int, n: int) -> int:
        # self._findMaxForm(['110', '11'],2,2) == 3, 'test1'
        # self._findMaxForm(['110', '1100'],2,2) == 4, 'test2'
        # self._findMaxForm(['1100', '1100'],1,1) == 0, 'test3'
        return self._findMaxForm(strs, m, n)

    def _findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # m is 0
        # n is 1
        # use knapsack
        def count_zero(s):
            cnt = [0, 0]
            for ch in s:
                cnt[ord(ch) - ord('0')] += 1
            return cnt

        dp = [[0] * (n + m + 1) for _ in range(n + m + 1)]
        for s in strs:
            cnt = count_zero(s)
            for z in range(m, cnt[0] - 1, -1):
                for e in range(n, cnt[1] - 1, -1):
                    dp[z][e] = max(1 + dp[z - cnt[0]][e - cnt[1]], dp[z][e])
        return dp[m][n]