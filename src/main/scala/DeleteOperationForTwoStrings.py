class Solution:
    def minDistance(self, word1, word2):
        if not word1 and not word2 or word1 == word2:
            return 0
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            for j in range(len(word1) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


sol = Solution()
print(sol.minDistance("algorithm", "altruistic"))  # 9
print(sol.minDistance("food", "money"))  # 7
print(sol.minDistance("a", "a"))
print(sol.minDistance("sea", "eat"))
