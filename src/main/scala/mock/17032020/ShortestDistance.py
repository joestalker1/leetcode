from heapq import heappush,heappop


class Solution:
    def shortestDistance(self, maze, start, destination):
        min_dist = [[float('inf')] * len(maze[0]) for _ in range(len(maze))]
        q = [[0, start[0],start[1]]]
        min_dist[start[0]][start[1]] = 0
        while q:
            d,r,c = heappop(q)
            if min_dist[r][c] < d: # can't relax [r,c]
                continue

            for dr,dc in [[1,0],[-1,0],[0,-1],[0,1]]:
                r1 = r + dr
                c1 = c + dc
                cost = 0
                while 0 <= r1 < len(maze) and 0 <= c1 < len(maze[0]) and maze[r1][c1] == 0:
                    cost += 1
                    r1 += dr
                    c1 += dc
                r1 -= dr
                c1 -= dc
                if min_dist[r1][c1] > min_dist[r][c] + cost:
                    min_dist[r1][c1] = min_dist[r][c] + cost
                    heappush(q, [min_dist[r1][c1], r1, c1])
        return -1 if min_dist[destination[0]][destination[1]] == float('inf') else min_dist[destination[0]][destination[1]]

sol = Solution()
print(sol.shortestDistance())