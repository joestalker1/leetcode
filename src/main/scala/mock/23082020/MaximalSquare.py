class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0] * m for _ in range(n)]
        max_len = 0
        # horz_max
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    d = 0
                    if i + 1 < n and j + 1 < m and matrix[i + 1][j + 1] == '1' and matrix[i][j+1] == '1' and matrix[i+1][j] == '1':
                        continue
                    elif i - 1 >= 0 and j -1 >= 0 and matrix[i - 1][j - 1] == '1' and matrix[i][j-1] == '1' and matrix[i-1][j] == '1':
                        dp[i][j] += dp[i][j-1]
                    elif i - 1 >= 0 and j + 1 < m and matrix[i - 1][j + 1] == '1' and matrix[i][j+1] == '1' and matrix[i-1][j] == '1':
                        continue
                    elif i + 1 < n and j - 1 >= 0 and matrix[i + 1][j - 1] == '1' and matrix[i+1][j] == '1' and matrix[i][j-1] == '1':
                        dp[i][j] += dp[i][j - 1]
                    max_len = max(max_len, dp[i][j])

        dp = [[0] * m for _ in range(n)]
        # vert_max
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i][j] = 1
                    d = 0
                    if j - 1 >= 0 and matrix[i][j - 1] == '1':
                        d += 1
                    if i - 1 >= 0 and matrix[i - 1][j] == '1':
                        d += 1
                    if d == 2:
                        dp[i][j] += dp[i - 1][j]
                    max_len = max(max_len, dp[i][j])
        return max_len * max_len


sol = Solution()
print(sol.maximalSquare(
    [['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']]))
