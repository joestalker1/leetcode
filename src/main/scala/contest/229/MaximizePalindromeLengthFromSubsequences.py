class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        h = m + n
        # find max polindromic subsequence
        word = word1 + word2
        dp = [[0] * h for _ in range(h)]
        for i in range(h):
            dp[i][i] = 1
        for l in range(2, h + 1):
            for i in range(h - l + 1):
                j = i + l - 1
                if word[i] == word[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        # go through and find such dp[i][j] that has i < n and j >= n
        max_len = 0
        # consider polindromic strings if one is in word1 and another is in word2
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:
                    max_len = max(max_len, dp[i][j + n])

        return max_len