class Solution:
    def islandPerimeter(self, grid):
        land = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    land.append((i, j))
        p = 0
        for i, j in land:
            if i - 1 >= 0 and grid[i - 1][j] == 0 or i - 1 < 0:
                p += 1
            if j - 1 >= 0 and grid[i][j - 1] == 0 or j - 1 < 0:
                p += 1
            if i + 1 < len(grid) and grid[i + 1][j] == 0 or i + 1 >= len(grid):
                p += 1
            if j + 1 < len(grid[0]) and grid[i][j + 1] == 0 or j + 1 >= len(grid[0]):
                p += 1
        return p


sol = Solution()
p = [[0, 1, 0, 0],
     [1, 1, 1, 0],
     [0, 1, 0, 0],
     [1, 1, 0, 0]]
print(sol.islandPerimeter(p))
