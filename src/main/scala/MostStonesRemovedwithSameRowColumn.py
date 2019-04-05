class Solution:
    def removeStones(self, stones):
        if not stones:
            return 0
        rows = {}
        cols = {}
        for i in range(len(stones)):
            i1,j1 = stones[i]
            if i1 not in rows:
                rows[i1] = set()
            if j1 not in cols:
                cols[j1] = set()
            rows[i1].add(i)
            cols[j1].add(i)

        def dfs(x, y, removed, moves):
            max_moves = moves
            if x in rows:
                for j in rows[x]:
                    if j in removed:
                        continue
                    removed.add(j)
                    res = dfs(stones[j][0],stones[j][1], removed, moves + 1)
                    removed.remove(j)
                    max_moves = max(res, max_moves)

            if y in cols:
                for j in cols[y]:
                    if j in removed:
                        continue
                    removed.add(j)
                    res = dfs(stones[j][0],stones[j][1], removed, moves + 1)
                    removed.remove(j)
                    max_moves = max(res, max_moves)
            return max_moves
        removed = set()
        max1 = 0
        for i in range(len(stones)):
            removed.add(i)
            x, y = stones[i]
            max1 = max(dfs(x,y, removed, 0), max1)
            removed.remove(i)
        return max1

sol = Solution()
print(sol.removeStones([[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]])) #4
#print(sol.removeStones([[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]))
#print(sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
#print(sol.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
#print(sol.removeStones([[0, 0]]))
