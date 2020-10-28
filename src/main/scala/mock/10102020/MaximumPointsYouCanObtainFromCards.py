class Solution:
    def maxScore(self, cardPoints, k: int):
        n = len(cardPoints)
        dp = [[0] * n for _ in range(n)]
        max_score = 0
        for l in range(max(n - k, 0), n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n:
                    continue
                if l == 2:
                    dp[i][j] = cardPoints[i] + cardPoints[j]
                elif l > 2:
                    dp[i][j] = max(cardPoints[i] + dp[i + 1][j], cardPoints[j] + dp[i][j - 1])
                max_score = max(max_score, dp[i][j])
        return max_score


sol = Solution()
#print(sol.maxScore([11, 49, 100, 20, 86, 29, 72], 4))  # 232
#print(sol.maxScore([9, 7, 7, 9, 7, 7, 9], 7))  # 55
print(sol.maxScore([1, 1000, 1], 1))
print(sol.maxScore([2, 2, 2], 2))
