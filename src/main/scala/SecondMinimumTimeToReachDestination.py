from collections import defaultdict
import heapq


class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:
        if not edges:
            return 0
        dp = [[] for _ in range(n + 1)]
        dp[1] = [0]
        adj_list = defaultdict(list)
        for v,u in edges:
            adj_list[v].append(u)
            adj_list[u].append(v)
        min_heap = [(0,1)]
        while min_heap:
            cur_time,node = heapq.heappop(min_heap)
            if node == n and len(dp[n]) == 2:
                return max(dp[n])
            if (cur_time // change) % 2 == 0:
                cur_time = cur_time + time
            else:
                cur_time = cur_time + time + change - (cur_time % change)
            for nei in adj_list[node]:
                if not dp[nei] or len(dp[nei]) == 1 and dp[nei] != [cur_time]:
                    dp[nei].append(cur_time)
                    heapq.heappush(min_heap, (cur_time, nei))