from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges) -> int:
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(adj_list, v, d, seen):
            seen.add(v)
            if v == d:
                return True
            for nei in adj_list[v]:
                if nei in seen:
                    continue
                if dfs(adj_list, nei, d, seen):
                    return True
            return False

        res = 0
        for a in range(n-1):
            need_vert = n - 1 - a
            reached = 0
            for b in range(a+1, n):
                if dfs(adj_list,a,b,set()):
                    reached += 1
            res += need_vert - reached
        return res


sol = Solution()
print(sol.countPairs(5,[[1,0],[3,1],[0,4],[2,1]]))#0
print(sol.countPairs(7,[[0,2],[0,5],[2,4],[1,6],[5,4]]))#14
