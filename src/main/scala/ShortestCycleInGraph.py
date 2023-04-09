from collections import defaultdict
import math
class Solution:
    def findShortestCycle(self, n: int, edges) -> int:
        # assert self._findShortestCycle(7,[[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]) == 3,'test1'
        # assert self._findShortestCycle(4, [[0,1],[0,2]]) == -1, 'test2'
        return self._findShortestCycle(n, edges)

    def _findShortestCycle(self, n: int, edges) -> int:
        adj_list= defaultdict(list)
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def bfs(adj_list, u):
            q = [u]
            dist = [math.inf] * n
            dist[u] = 0
            par = [-1] * n
            min_len = math.inf
            while q:
                node = q.pop(0)
                for v in adj_list[node]:
                    if dist[v] == math.inf:
                        dist[v] = dist[node] + 1
                        par[v] = node
                        q.append(v)
                    elif par[v] != node and par[node] != v:
                        min_len = min(min_len, dist[v] + dist[node] + 1)
            return min_len

        min_len = math.inf
        for v in range(n):
            min_len = min(min_len, bfs(adj_list, v))
        return min_len if min_len < math.inf else -1