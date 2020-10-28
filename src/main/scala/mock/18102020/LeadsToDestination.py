from collections import defaultdict


class Solution:
    def leadsToDestination(self, n: int, edges, source, destination):
        adj_list = defaultdict(list)

        for s, d in edges:
            adj_list[s].append(d)
        ended = 0
        cycle = False
        def dfs(adj_list, u, seen):
            nonlocal ended, cycle
            if u == destination:
                ended += 1
                return
            for v in adj_list[u]:
                if v in seen:
                    cycle = True
                    continue
                seen.add(v)
                dfs(adj_list, v, seen)

        for u in adj_list[source]:
            seen = set()
            seen.add(source)
            dfs(adj_list, u, seen)
        return ended == len(adj_list[source]) and not cycle


sol = Solution()
print(sol.leadsToDestination(3,[[0,1],[1,1],[1,2]],0, 2))#false
print(sol.leadsToDestination(3, [[0, 1], [0, 2]], 0, 2))#false

print(sol.leadsToDestination(4, [[0, 1], [0, 2], [1, 3], [2, 3]], 0, 3))#true
