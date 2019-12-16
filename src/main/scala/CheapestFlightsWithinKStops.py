from collections import defaultdict
from heapq import heappop,heappush,heapify

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        if n == 0 or not flights:
            return -1
        adj_list = defaultdict(list)
        for s,e,w in flights:
            adj_list[s].append((w, e)) # weight, dest

        dist = [float('inf')] * n
        dist[0] = 0
        len_path = [-1] * n
        q = []
        heappush(q, (0,src))
        len_path[src] = 1
        max_len = K + 2# count src and dst
        seen = set()
        while q:
            _,u = heappop(q)
            seen.add(u)
            for w,v in adj_list[u]:
                if v not in seen and dist[u] + w < dist[v]:
                    if (v != dst and len_path[u] + 1 < max_len) or (v == dst and len_path[u] + 1 <= max_len):
                        dist[v] = dist[u] + w
                        len_path[v] = len_path[u] + 1
                        heappush(q, (dist[v], v))
        return dist[dst] if dist[dst] != float('inf') else -1


sol = Solution()
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],0, 2, 0))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],0, 2, 1))






