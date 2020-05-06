class Solution(object):
    def longestPalindromeSubseq(self, s):
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        max_len = 1
        for len_s in range(2, len(s) + 1):
            for i in range(len(s) - len_s + 1):
                j = i + len_s - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return max_len