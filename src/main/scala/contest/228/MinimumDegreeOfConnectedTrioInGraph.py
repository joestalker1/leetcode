from collections import defaultdict
import math

class Solution:
    def minTrioDegree(self, n: int, edges):
        vertices = []
        for a, b in edges:
            vertices.append(sorted([a, b]))
        vertices.sort()
        adj_list = defaultdict(set)
        for a, b in edges:
            adj_list[a].add(b)
            adj_list[b].add(a)

        res = math.inf
        for i in range(len(vertices) - 2):
            a, b = vertices[i]
            d1 = len(adj_list[a])
            d2 = len(adj_list[b])
            if d1 < 2 or d2 < 2:
                continue
            for j in range(i + 1, len(vertices)):
                c, d = vertices[j]
                if c != a:
                    break
                # a == c, then try to find (b,d)
                if b in adj_list and d in adj_list[b]:
                    d3 = len(adj_list[d])
                    res = min(res, d1 + d2 + d3 - 6)
        return res if res != math.inf else -1