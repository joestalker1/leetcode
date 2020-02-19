class Solution:
    def longestCommonSubsequence(self, text1, text2):
        if not text1 or not text2:
            return 0
        dp = [[0] * len(text1) for _ in range(len(text2))]
        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    dp[i][j] = 1
                    if i > 0 and j > 0:
                        dp[i][j] += dp[i-1][j - 1]
                if i > 0:
                    dp[i][j] = max(dp[i-1][j], dp[i][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j-1], dp[i][j])
        return dp[len(text2) - 1][len(text1) - 1]


sol = Solution()
print(sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))#1
print(sol.longestCommonSubsequence(text1 = "abcde", text2 = "ace" ))#3
