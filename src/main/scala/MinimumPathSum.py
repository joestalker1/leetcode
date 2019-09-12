class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0
        sum_mat = [0] * len(grid)
        for i in range(len(sum_mat)):
            sum_mat[i] = [0] * len(grid[0])

        sum_mat[0][0] = grid[0][0]
        for i, col in enumerate(grid):
            for j,x in enumerate(col):
                if i > 0 and j > 0:
                    sum_mat[i][j] = min(sum_mat[i-1][j] + x, sum_mat[i][j-1] + x)
                elif i > 0:
                    sum_mat[i][j] = sum_mat[i-1][j] + x
                elif j > 0:
                    sum_mat[i][j] = sum_mat[i][j - 1] + x
        return sum_mat[-1][-1]


sol = Solution()
print(sol.minPathSum(
  [[1,3,1],
  [1,5,1],
  [4,2,1]]))






