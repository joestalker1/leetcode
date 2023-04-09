class Solution:

    def isPossibleToCutPath(self, grid) -> bool:
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 2:
            return False

        def find_path(r, c):
            if r == n - 1 and c == m - 1:
                return True
            grid[r][c] = 0
            #go to bottom
            if r + 1 < n and grid[r+1][c] == 1 and find_path(r+1,c):
                return True
            # go to the right:
            if c + 1 < m and grid[r][c+1] == 1 and find_path(r,c + 1):
                return True
            return False

        if find_path(0, 0) and find_path(0,0):
            return False
        return True
