import math

class Solution:
    def waysToBuildRooms(self, arr) -> int:
        MOD = 10 ** 9 + 7
        # build adjacent list
        graph = collections.defaultdict(list)
        for i, v in enumerate(arr):
            graph[v].append(i)

        def dfs(graph, node):
            ways = 1
            # node number
            cnt = 0
            for nei in graph[node]:
                cnt1, ways1 = dfs(graph, nei)
                ways = (ways1 * ways * math.comb(cnt + cnt1, cnt1)) % MOD
                cnt += cnt1
            return cnt + 1, ways

        return dfs(graph, 0)[1]