from heapq import heappop, heappush
from collections import defaultdict

MAX = float('inf')


class Solution:
    def networkDelayTime(self, times, N, K):
        if not times or N == 0:
            return -1

        adj_list = defaultdict(list)
        for s, e, t in times:
            adj_list[s].append([e, t])

        q = [[0, K]]
        dist = [MAX] * (N + 1)
        dist[0] = 0
        dist[K] = 0
        while q:
            cur,node = heappop(q)
            for nei,t in adj_list[node]:
                if cur + t < dist[nei]:
                    dist[nei] = cur + t
                    heappush(q, [dist[nei], nei])
        return max(dist) if all([True if x != MAX else False for x in dist]) else -1
