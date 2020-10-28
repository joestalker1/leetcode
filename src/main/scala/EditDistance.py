class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if n * m == 0:
            return n + m
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # n chars are needed to remove
        for i in range(n + 1):
            dp[0][i] = i
        # m chars are needed to remove
        for i in range(m + 1):
            dp[i][0] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # insert char to word2, add 1 to edit distance for dp[i][j]
                left = dp[i][j - 1] + 1
                # insert char to word1, so add 1 to dp[i][j]
                down = dp[i - 1][j] + 1
                # don't need to increase edit distance in dp[i][j]
                left_right = dp[i - 1][j - 1]
                if word1[j - 1] != word2[i - 1]:
                    # if current chars differ, increase dp[i][j]
                    left_right += 1
                dp[i][j] = min(left, down, left_right)
        return dp[-1][-1]

