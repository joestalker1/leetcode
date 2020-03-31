class Solution:
    def minHours(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0
        changed = False
        for i, row in enumerate(grid):
            for j, a in enumerate(row):
                if a == 0:
                    continue
                if a == 1:
                    if i - 1 >= 0 and grid[i - 1][j] == 0:
                        changed = True
                        grid[i - 1][j] = -1
                    if i + 1 < len(grid) and grid[i + 1][j] == 0:
                        changed = True
                        grid[i + 1][j] = -1
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        changed = True
                        grid[i][j - 1] = -1
                    if j + 1 < len(grid[0]) and grid[i][j + 1] == 0:
                        grid[i][j + 1] = -1
                elif a == -1:
                    grid[i][j] = 1
        if changed:
            return 1 + self.minHours(grid)
        return 0


sol = Solution()
print(sol.minHours([[0, 1, 1, 0, 1],
                    [0, 1, 0, 1, 0],
                    [0, 0, 0, 0, 1],
                    [0, 1, 0, 0, 0]]))
