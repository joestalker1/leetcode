from collections import defaultdict


class Solution:

    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        if not red_edges and not blue_edges:
            ans = [-1]*n
            ans[0] = 0
            return ans
        MAX = float('inf')
        adj_list = defaultdict(list)
        # path_len = [[MAX] * n for _ in range(n)]
        # 0 is red,1 is blue,2 is gray
        for x, y in red_edges:
            adj_list[x].append([0, y])
        for x, y in blue_edges:
            adj_list[x].append([1, y])

        ans = [[MAX, MAX] for _ in range(n)]
        ans[0][0] = 0
        ans[0][1] = 0
        q = [[0, 0], [0, 1]]  # node,clr
        while q:
            node, clr = q.pop(0)
            for nei_clr, nei in adj_list[node]:
                if nei_clr == 1 - clr and ans[nei][nei_clr] > ans[node][clr] + 1:
                        ans[nei][nei_clr] = ans[node][clr] + 1
                        q.append([nei, nei_clr])
        return [min(a1,a2) if min(a1,a2) != MAX else -1 for a1,a2 in ans]


sol = Solution()
# print(sol.shortestAlternatingPaths(3,
#                                    [[0, 1], [0, 2]],
#                                    [[1, 0]]))
print(sol.shortestAlternatingPaths(5,
                                   [[3, 2], [4, 1], [1, 4], [2, 4]],
                                   [[2, 3], [0, 4], [4, 3], [4, 4], [4, 0], [1, 0]]))  # [0, 2, -1, -1, 1]
print(sol.shortestAlternatingPaths(5,
                                   [[0, 1], [1, 2], [2, 3], [3, 4]],
                                   [[1, 2], [2, 3], [3, 1]]))  # [0, 1, 2, 3, 7]
print(sol.shortestAlternatingPaths(n=3, red_edges=[[1, 0]], blue_edges=[[2, 1]]))  # [0,-1,-1]
print(sol.shortestAlternatingPaths(n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]))
print(sol.shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]]))
