from collections import defaultdict
from heapq import heappop,heappush
from math import inf

class Solution:
    def countRestrictedPaths(self, n: int, edges):
        adj_list = defaultdict(list)
        for s,e,w in edges:
            adj_list[s].append([w, e])
            adj_list[e].append([w,s])
        dist = [inf] * (n + 1)
        #find short path for i
        q = [[0, n]]
        dist[n] = 0
        #use Dikjistra
        while q:
            _,node = heappop(q)
            for w,nei in adj_list[node]:
                if dist[nei] > dist[node] + w:
                    dist[nei] = dist[node] + w
                    heappush(q,[dist[nei],nei] )

        def dfs(dist, adj_list, x, mem):
            if x in mem:
                return mem[x]
            if x == n:
                return 1
            res = 0
            for w,nei in adj_list[x]:
                if dist[x] > dist[nei]:
                    res = (res + dfs(dist, adj_list, nei, mem)) % (10 ** 9 + 7)
            mem[x] = res
            return mem[x]
        return dfs(dist, adj_list, 1, {})

sol = Solution()
#print(sol.countRestrictedPaths(n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]))#1
print(sol.countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))#3





