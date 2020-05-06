class Solution:
    def generateMatrix(self, n: int):
        if n == 0:
            return []
        A = [[0] * n for _ in range(n)]
        i, j, dx, dy = 0, 0, 0, 1
        for k in range(n * n):
            A[i][j] = k + 1
            print('{} {}'.format(dx,dy))
            if A[(i + dx) % n][(j + dy) % n]:
                dx, dy = dy, -dx
            i += dx
            j += dy
        return A


sol = Solution()
print(sol.generateMatrix(6))


