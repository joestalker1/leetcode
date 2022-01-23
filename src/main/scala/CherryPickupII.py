class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dirs = [0, 1, -1]

        @lru_cache(None)
        def pick_cherry(r1, c1, c2):
            nonlocal dirs
            if r1 == len(grid):
                return 0
            r2 = r1
            max_cherry = 0
            for dc1 in dirs:
                nc1 = c1 + dc1
                nr1 = r1 + 1
                if nc1 == len(grid[0]) or nc1 < 0:
                    continue
                for dc2 in dirs:
                    nc2 = c2 + dc2
                    if nc2 == len(grid[0]) or nc2 < 0 or nc1 >= nc2:
                        continue
                    max_cherry = max(max_cherry, grid[r1][c1] + grid[r1][c2] + pick_cherry(nr1, nc1, nc2))
            return max_cherry

        return pick_cherry(0, 0, m - 1)
