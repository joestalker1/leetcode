class Solution:
    def numSubmat(self, mat):
        n = len(mat)
        m = len(mat[0])
        h = [0] * m
        res = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    h[j] += 1
                else:
                    h[j] = 0
            for l in range(m):
                k = l
                t = float('inf')
                while k < m and h[k] != 0:
                    t = min(t, h[k])
                    res += t
                    k += 1
        return res


sol = Solution()
print(sol.numSubmat([[1, 0, 1], [1, 1, 0], [1, 1, 0]]))
