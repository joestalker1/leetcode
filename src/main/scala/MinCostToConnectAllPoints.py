class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, p):
        if self.par[p] != p:
            self.par[p] = self.find(self.par[p])
        return self.par[p]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.rank[p1] += 1
            self.par[p2] = p1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]):
        # assert self._minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20, 'test1'
        return self._minCostConnectPoints(points)

    def _minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edge = []
        for i in range(n):
            for j in range(i + 1, n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edge.append((w, i, j))
        edge.sort()
        used_edges = 0
        mst = 0
        uf = UnionFind(n)
        for w, s, e in edge:
            if uf.union(s, e):
                mst += w
                used_edges += 1
                if used_edges == n - 1:
                    break
        return mst








