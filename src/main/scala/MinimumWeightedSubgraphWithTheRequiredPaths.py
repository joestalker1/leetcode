from math import inf
from heapq import heappop,heappush
from collections import defaultdict

class Solution:
    def minimumWeight(self, n: int, edges, src1: int, src2: int, dest: int) -> int:

        def dijkstra(graph, K):
            q, t = [(0, K)], {}
            while q:
                time, node = heappop(q)
                if node not in t:
                    t[node] = time
                    for v, w in graph[node]:
                        heappush(q, (time + w, v))
            return [t.get(i, float("inf")) for i in range(n)]

        adj_list = defaultdict(list)
        rev_adj_list = defaultdict(list)
        for s, e, w in edges:
            adj_list[s].append((e, w))
            rev_adj_list[e].append((s, w))
        visited1 = dijkstra(adj_list, src1)
        visited2 = dijkstra(adj_list, src2)
        visited3 = dijkstra(rev_adj_list, dest)
        min_weight = inf
        for v in range(n):
            min_weight = min(min_weight, visited1[v] + visited2[v] + visited3[v])
        return min_weight if min_weight != inf else -1