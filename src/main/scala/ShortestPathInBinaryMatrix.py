class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        if not grid or len(grid[0]) == 0 or grid[-1][-1] == 1 or grid[0][0] == 1:
            return -1
        n = len(grid)
        m = len(grid[0])
        q = [(0, 0)]
        min_dist = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        while q:
            sz = len(q)
            min_dist += 1
            for _ in range(sz):
                r, c = q.pop(0)
                if r == n - 1 and c == m - 1:
                    return min_dist
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                        q.append((nr, nc))
                        grid[nr][nc] = -1
        return -1

