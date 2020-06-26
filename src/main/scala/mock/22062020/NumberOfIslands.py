class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        if len(grid) == 1:
            return grid[0]
        lands = 0
        n = len(grid)
        m = len(grid[0])
        parent = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    lands += 1
                    parent[(i, j)] = (i, j)

        def find(par, rc):
            if par[rc] != rc:
                par[rc] = find(par, par[rc])
            return par[rc]

        def union(par, rc1, rc2):
            nonlocal lands
            p1 = find(par, rc1)
            p2 = find(par,rc2)
            if p2 == p1:
                return
            par[p1] = p2
            lands -= 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0':
                    continue
                for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
                    r = i + dr
                    c = j + dc
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == '1':
                        union(parent, (i, j), (r, c))
                grid[i][j] = '0'
        return lands


sol = Solution()
print(sol.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
