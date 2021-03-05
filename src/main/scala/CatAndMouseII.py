from functools import lru_cache

class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        n = len(grid)
        m = len(grid[0])

        cat = None
        mouse = None
        aval = 0
        #count available cells in grid
        for r,line in enumerate(grid):
            for c in range(len(line)):
                if grid[r][c] != '#':
                    aval += 1
                if grid[r][c] == 'C':
                    cat = (r,c)
                elif grid[r][c] == 'M':
                    mouse = (r,c)
        #cache a reuslt by key(cat,mouse, turn)
        @lru_cache(None)
        def dfs(cat, mouse, turn):
            #cell number are twice for cat and mouse moves
            if turn == (2 * aval):
                return False

            steps = catJump if turn % 2 == 1 else mouseJump
            # go in on direction
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                for d in range(steps + 1):
                    #cat move
                    if turn % 2 == 1:
                        nr = cat[0] + dr * d
                        nc = cat[1] + dc * d
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                            if (nr, nc) == mouse or grid[nr][nc] == 'F' or not dfs((nr,nc), mouse, turn + 1):
                                return False
                        else:
                            #stop going
                            break
                    else:
                        #mouse move
                        nr = mouse[0] + dr * d
                        nc = mouse[1] + dc * d
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] != '#':
                            if grid[nr][nc] == 'F' or dfs(cat, (nr,nc), turn + 1):
                                return True
                        else:
                            #stop going
                            break
            #important:
            # if cat can't catch either mouse or food then mouse wins
            if turn % 2 == 0:
                return False
            #otherwise cat wins and mouse looses
            return True
        return dfs(cat, mouse, 0)

sol = Solution()
print(sol.canMouseWin(["M.C...F"], 1, 3))#false
print(sol.canMouseWin(["M.C...F"], 1, 4))#True

