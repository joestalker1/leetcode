class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        count = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i-1][j-1] == 1:
                    sz = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                    count += sz
                    dp[i][j] = sz
        return count


                    

