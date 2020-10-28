from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections):
        new_edges = 0
        adj_list = defaultdict(list)
        edges = set()
        for x,y in connections:
            adj_list[x].append(y)
            adj_list[y].append(x)
            edges.add((x,y))
        seen = set()
        seen.add(0)
        q = [0]
        while q:
            n = q.pop(0)
            for v in adj_list[n]:
                if v in seen:
                    continue
                if (n,v) in edges:
                    new_edges += 1
                q.append(v)
                seen.add(v)
        return new_edges
