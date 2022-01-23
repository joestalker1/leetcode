class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = []
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i, j])
        if len(q) == len(grid) * len(grid[0]):
            return -1
        dist = 0
        while q:
            dist += 1
            cur_size = len(q)
            for _ in range(cur_size):
                x, y = q.pop(0)
                for dx, dy in dir:
                    nx = x + dx
                    ny = y + dy
                    # if it's water,let's assign it to min_dist
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                        grid[nx][ny] = dist
                        q.append([nx, ny])
        return dist - 1 if dist > 0 else -1
