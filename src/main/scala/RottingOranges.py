class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return -1
        rotten = []
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))
                elif grid[i][j] == 1:
                    cnt += 1
        minutes = 0
        while rotten:
            r, c, minutes = rotten.pop(0)
            if r + 1 < len(grid) and grid[r + 1][c] == 1:
                grid[r + 1][c] = 2
                cnt -= 1
                rotten.append((r + 1, c, minutes + 1))
            if r - 1 >= 0 and grid[r - 1][c] == 1:
                grid[r - 1][c] = 2
                cnt -= 1
                rotten.append((r - 1, c, minutes + 1))
            if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                grid[r][c + 1] = 2
                cnt -= 1
                rotten.append((r, c + 1, minutes + 1))
            if c - 1 >= 0 and grid[r][c - 1] == 1:
                grid[r][c - 1] = 2
                cnt -= 1
                rotten.append((r, c - 1, minutes + 1))
        if cnt == 0:
            return minutes
        return -1

