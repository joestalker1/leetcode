from collections import defaultdict
from heapq import heappop,heappush
from math import inf

class Solution:
    def countPaths(self, n: int, roads) -> int:
        adj_lst = defaultdict(list)
        for u,v,t in roads:
            adj_lst[u].append([v, t])
            adj_lst[v].append([u, t])
        dist = [inf] * n
        dist[0] = 0
        path = [0] * n
        path[0] = 1
        mod = 10 ** 9 + 7
        q = [[0,0]]
        while q:
            d,v = heappop(q)
            #prevent to go back
            if dist[v] < d:
                continue
            for nei,t in adj_lst[v]:
                if d + t < dist[nei]:
                    path[nei] = path[v]
                    dist[nei] = d + t
                    heappush(q, [dist[nei], nei])
                elif d + t == dist[nei]:
                    # we go through v few times
                    path[nei] = (path[nei] + path[v]) % mod
        return path[n-1]


sol = Solution()
print(sol.countPaths(5,[[0,1,1],[1,2,4],[0,4,3],[3,2,5],[3,4,1],[3,0,5],[1,3,1]]))#2

print(sol.countPaths(n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))#4