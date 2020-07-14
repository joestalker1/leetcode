class Solution(object):
    def minSwapsCouples(self, row):
        N = len(row) // 2
        couples = [[] for _ in range(N)]
        for i, x in enumerate(row):
            couples[x // 2].append(i // 2)

        adj = [[] for _ in range(N)]
        for x, y in couples:
            adj[x].append(y)
            adj[y].append(x)

        ans = N
        for start in range(N):
            if not adj[start]:
                continue
            ans -= 1
            x, y = start, adj[start].pop()

            while y != start:
                adj[y].remove(x)
                x, y = y, adj[y].pop()
        return ans


sol = Solution()
print(sol.minSwapsCouples([0, 2, 1, 3, 4, 5, 6, 7]))
