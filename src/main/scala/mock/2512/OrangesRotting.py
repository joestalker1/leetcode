class Solution:
    def orangesRotting(self, grid):
        if not grid:
            return -1
        cnt = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    cnt += 1
        minutes = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    f = False
                    if r - 1 >= 0 and grid[r - 1][c] == 1:
                        grid[r - 1][c] = 2
                        cnt -= 1
                        f = True
                    if r + 1 < len(grid) and grid[r + 1][c] == 1:
                        grid[r + 1][c] = 2
                        cnt -= 1
                        f = True
                    if c - 1 >= 0 and grid[r][c - 1] == 1:
                        grid[r][c - 1] = 2
                        cnt -= 1
                        f = True
                    if c + 1 < len(grid[0]) and grid[r][c + 1] == 1:
                        grid[r][c + 1] = 2
                        cnt -= 1
                        f = True
                    if f:
                        minutes += 1

        if cnt == 0:
            return minutes
        return -1


sol = Solution()
print(sol.orangesRotting([[1],[2],[2]]))
print(sol.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
