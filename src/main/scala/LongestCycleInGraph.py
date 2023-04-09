class Solution:
    def longestCycle(self, edges) -> int:
        # assert self._longestCycle([1,-1]) == -1, 'test1'
        # assert self._longestCycle([3,3,4,2,3]) == 3, 'test2'
        return self._longestCycle(edges)

    def _longestCycle(self, edges) -> int:
        n = len(edges)

        def dfs(edges, dist, seen, v):
            nonlocal max_len
            seen.add(v)
            node = edges[v]
            if node != -1 and node not in seen:
                dist[node] = dist[v] + 1
                dfs(edges, dist, seen, node)
            elif node != -1 and node in dist:
                #we visited node before.
                max_len = max(max_len, dist[v] - dist[node] + 1)

        max_len = -1
        seen = set()
        for u in range(n):
            if u in seen:
                continue
            dist = {}
            dist[u] = 1
            dfs(edges, dist,seen, u)
        return max_len