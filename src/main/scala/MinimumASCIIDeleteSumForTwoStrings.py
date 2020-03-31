class Solution:
    def minimumDeleteSum(self, s1, s2):
        dp = [[0] * (len(s1) + 1) for _ in range(len(s2) + 1)]

        for i in range(len(s2) - 1, - 1, -1):
            dp[i][len(s1)] = ord(s2[i]) + dp[i + 1][len(s1)]
        for i in range(len(s1) - 1, -1, -1):
            dp[len(s2)][i] = ord(s1[i]) + dp[len(s2)][i + 1]

        for i in range(len(s2) - 1, -1, -1):
            for j in range(len(s1) - 1, -1, -1):
                if s2[i] == s1[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s2[i]), dp[i][j+1] + ord(s1[j]))
        return dp[0][0]


sol = Solution()
print(sol.minimumDeleteSum("sea", "eat"))
