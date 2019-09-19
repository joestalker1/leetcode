class Solution:
    def count_nearby_land_grid(self, grid, x, y):
        lands = 0
        if x > 0 and grid[x-1][y] == 1:
            lands += 1
        if x < len(grid) - 1 and grid[x + 1][y] == 1:
            lands += 1
        if y > 0 and grid[x][y - 1] == 1:
            lands += 1
        if y < len(grid[0]) - 1 and grid[x][y + 1] == 1:
            lands += 1
        return lands

        return 0
    def islandPerimeter(self, grid):
        if not grid:
            return 0
        perim = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perim_grid = 4 - self.count_nearby_land_grid(grid, i, j)
                    perim += perim_grid
        return perim


sol = Solution()
print(sol.islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))