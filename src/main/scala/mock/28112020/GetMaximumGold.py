class Solution:
    def getMaximumGold(self, grid):
        if not grid or not grid[0]:
            return 0

        n = len(grid)
        m = len(grid[0])

        def dfs(r,c):
            # if (r,c) in mem:
            #     return mem[(r,c)]
            max_gold = 0
            for dr,dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m and (nr,nc) not in seen and grid[nr][nc] > 0:
                    t= grid[r][c]
                    grid[r][c] = -1
                    gold = grid[nr][nc] + dfs(nr, nc, mem)
                    grid[r][c] = t
                    max_gold = max(gold, max_gold)
            mem[(r,c)] = max_gold
            return max_gold
        max_gold = 0
        mem = {}
        for r in range(n):
            for c in range(m):
                if grid[r][c]:
                    t = grid[r][c]
                    grid[r][c] = -1
                    max_gold = max(grid[r][c] + dfs(r,c, mem), max_gold)
                    grid[r][c] = t
        return max_gold