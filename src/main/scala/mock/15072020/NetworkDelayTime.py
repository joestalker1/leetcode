from collections import defaultdict


class Solution:
    def networkDelayTime(self, times, N, K):
        if not times or N == 0:
            return 0
        adj_list = defaultdict(list)
        for s, e, t in times:
            adj_list[s].append((e, t))

        q = [[K, 0]]
        # visited = set()
        # visited.add(K)
        MAX = float('inf')
        spent = [MAX] * (N + 1)
        spent[0] = 0
        spent[K] = 0
        while q:
            n, t = q.pop(0)
            for nei, tm in adj_list[n]:
                if t + tm < spent[nei]:
                    spent[nei] = t + tm
                    q.append([nei, t + tm])
        visited = sum([1 for t in spent if t != MAX])
        return max(spent) if visited == N+1 else -1


sol = Solution()
print(sol.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3,1))
