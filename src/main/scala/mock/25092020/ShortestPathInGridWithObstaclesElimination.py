from heapq import heappop, heappush


class Solution:
    def shortestPath(self, grid, k):
        if not grid or not grid[0]:
            return -1
        n = len(grid)
        m = len(grid[0])
        q = [[0, 0, 0, 0]]  # len, row,col, eliminated obstacles < k
        seen = set()
        seen.add((0,0))
        while q:
            d, r, c, elim = q.pop(0)
            if r == n - 1 and c == m - 1:
                return d
            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    # if (nr, nc) in seen:
                    #     continue
                    if grid[nr][nc] == 0 or grid[nr][nc] == 1 and elim < k:
                            paths[nr][nc] = d + 1
                            q.append([d + 1, nr, nc, elim + 1 if grid[nr][nc] == 1 else elim])
        return -1


sol = Solution()
# print(sol.shortestPath([[0, 0, 0],
#                         [1, 1, 0],
#                         [0, 0, 0],
#                         [0, 1, 1],
#                         [0, 0, 0]], 1))

print(sol.shortestPath([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                        [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]],
                       1))
