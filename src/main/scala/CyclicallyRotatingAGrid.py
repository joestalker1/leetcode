class Solution:
    def rotateGrid(self, grid, k: int):
        m = len(grid)
        n = len(grid[0])
        ll = min(m, n) // 2
        for l in range(ll):
            v = []
            # top right
            for i in range(l, n - l - 1):
                v.append(grid[l][i])
            # right
            for i in range(l, m - l - 1):
                v.append(grid[i][n - l - 1])
            # bottom
            for i in range(n - l - 1, l, -1):
                v.append(grid[m - l - 1][i])
            # left
            for i in range(m - l - 1, l, -1):
                v.append(grid[i][l])

            s = k % len(v)
            # top right
            for i in range(l, n - l - 1):
                grid[l][i] = v[s % len(v)]
                s += 1
            # right
            for i in range(l, m - l - 1):
                grid[i][n - l - 1] = v[s % len(v)]
                s += 1
            # bottom
            for i in range(n - l - 1, l, -1):
                grid[m - l - 1][i] = v[s % len(v)]
                s += 1
            # left
            for i in range(m - l - 1, l, -1):
                grid[i][l] = v[s % len(v)]
                s += 1
        return grid

