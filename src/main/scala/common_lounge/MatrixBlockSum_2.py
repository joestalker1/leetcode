class Solution:
    def matrixBlockSum(self, mat, K):
        n = len(mat)
        m = len(mat[0])
        pr = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                pr[i][j] = mat[i-1][j-1] + pr[i-1][j] + pr[i][j-1] - pr[i-1][j-1]

        res = [[0] * m for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                r1 = max(1, i - K)
                c1 = max(1, j - K)
                r2 = min(n, i + K)
                c2 = min(m, j + K)
                res[i-1][j-1] = pr[r2][c2] - pr[r1-1][c2] - pr[r2][c1-1]+ pr[r1-1][c1-1]
        return res
