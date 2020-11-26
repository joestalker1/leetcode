class Solution:
    def matrixBlockSum(self, mat, K):
        if not mat or K == 0:
            return mat
        n = len(mat)
        m = len(mat[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                s = 0
                for r in range(max(0, i - K), min(n, i + K + 1)):
                    for c in range(max(0, j - K), min(n, j + K + 1)):
                        s += mat[r][c]
                ans[i][j] = s
        return ans

