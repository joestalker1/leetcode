class Solution:
    def countSubIslands(self, grid1, grid2) -> int:
        island = 0

        def check_island(r, c):
            matched = True
            if grid1[r][c] == 0:
                matched = False
            grid2[r][c] = -1
            if r - 1 >= 0 and grid2[r - 1][c] == 1:
                if not check_island(r - 1, c):
                    matched = False
            if r + 1 < len(grid2) and grid2[r + 1][c] == 1:
                if not check_island(r + 1, c):
                    matched = False
            if c - 1 >= 0 and grid2[r][c - 1] == 1:
                if not check_island(r, c - 1):
                    matched = False
            if c + 1 < len(grid2[0]) and grid2[r][c + 1] == 1:
                if not check_island(r, c + 1):
                    matched = False
            return matched

        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] <= 0:
                    continue
                if check_island(i, j):
                    island += 1
        return island
