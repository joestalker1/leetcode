class Dsu:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        self.p[py] = px

class Solution:
    def removeStones(self, stones):
        if not stones:
            return 0
        dsu = Dsu(20000)
        for x,y in stones:
            dsu.union(x, y + 10000)
        comp = {dsu.find(x) for x, y in stones}
        return len(stones) - len(comp)


sol = Solution()
print(sol.removeStones([[0,1],[1,0],[1,1]])) #2
print(sol.removeStones([[3, 2], [3, 1], [4, 4], [1, 1], [0, 2], [4, 0]]))  # 4
print(sol.removeStones([[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]]))
# print(sol.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]))
# print(sol.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]))
# print(sol.removeStones([[0, 0]]))
