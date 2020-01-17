class Solution:
    def longest_common_subsequence1(self, a, b):
        if not a or not b:
            return 0

        mem = [[-1] * 1000 for _ in range(1000)]

        def lcs(i, j):
            if i == -1 or j == -1:
                return 0
            if mem[i][j] != -1:
                return mem[i][j]
            res = 0
            res = max(res, lcs(i, j - 1))
            res = max(res, lcs(i-1, j))
            if a[i] == b[j]:
                res = max(res, 1 + lcs(i - 1, j - 1))
            mem[i][j] = res
            return res
        return lcs(len(a) - 1, len(b) - 1)

    def longest_common_subsequence2(self, a, b):
        if not a or not b:
            return 0

        dp = [[0] * len(a) for _ in range(len(b))]
        if a[0] == b[0]:
            dp[0][0] = 1
        for i in range(1, len(b)):
            for j in range(1, len(a)):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if b[i] == a[j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[i-1][j-1])
        return dp[len(b) - 1][len(a) - 1]


sol = Solution()
print(sol.longest_common_subsequence2("aaaa", "aaaa"))