class Solution:
    def countSquares(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        h = [0] * m
        count = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1:
                    h[j] += 1
                else:
                    h[j] = 0

            for l in range(m):
                k = l
                t = n + m + 1
                while k < m and h[k] != 0:
                    t = min(t, h[k])
                    k += 1
                if t != n + m + 1:
                    d = k - l + 1
                    if d % t == 0:
                        count += d % t
        return count


