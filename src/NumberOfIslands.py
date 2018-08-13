class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "0":
                    continue
                count += 1
                q = list()
                q.append((j, i))
                while len(q) > 0:
                    xy = q.pop(0)
                    x = xy[0]
                    y = xy[1]
                    if grid[y][x] == "1":
                        if x - 1 >= 0 and grid[y][x - 1] == "1":
                            q.append((x - 1, y))
                        if x + 1 < len(grid[0]) and grid[y][x + 1] == "1":
                            q.append((x + 1, y))
                        if y - 1 >= 0 and grid[y - 1][x] == "1":
                            q.append((x, y - 1))
                        if y + 1 < len(grid) and grid[y + 1][x] == "1":
                            q.append((x, y + 1))
                    grid[y][x] = "0"
        return count

sol = Solution()
grid2 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
grid1 = [[1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]]
print(sol.numIslands(grid2))