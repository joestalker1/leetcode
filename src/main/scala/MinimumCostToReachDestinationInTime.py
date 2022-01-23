from math import *
from collections import *
from heapq import *

class Solution:
    def minCost(self, maxTime: int, edges, passingFees) -> int:
        # fee, vertex, time
        q = [(passingFees[0], 0, 0)]
        n = len(passingFees)
        times = [inf] * n
        adj_lst = defaultdict(list)
        for (s, e, t) in edges:
            adj_lst[s].append((e, t))
            adj_lst[e].append((s, t))

        while q:
            (fee, u, tu) = heapq.heappop(q)
            if tu > maxTime:
                continue
            if u == n - 1:
                return fee
            if times[u] > tu:
                times[u] = tu
                for (v, t) in adj_lst[u]:
                    heapq.heappush(q, (fee + passingFees[v], v, tu + t))
        return -1
