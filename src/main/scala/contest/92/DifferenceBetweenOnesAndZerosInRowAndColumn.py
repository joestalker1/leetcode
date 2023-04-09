class Solution:
    def onesMinusZeros(self, grid):
        n = len(grid)
        m = len(grid[0])
        one_row = [0] * n
        zero_col = [0] * m
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    one_row[i] += 1
                elif grid[i][j] == 0:
                    zero_col[j] += 1
        diff = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                diff[i][j] = one_row[i] + (n - zero_col[j]) - (m-one_row[i]) - zero_col[j]
        return diff


sol = Solution()
print(sol.onesMinusZeros([[1,1,1],[1,1,1]]))