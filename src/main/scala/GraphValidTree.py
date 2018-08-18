class Solution:
    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent,x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def validTree(self, n, edges):
        if n == 0 or not edges:
            return False
        parent = [i for i in range(n)]
        rank = [0] * n
        for edge in edges:
            x = self.find(parent, edge[0])
            y = self.find(parent, edge[1])
            if x == y:
                return False
            self.union(parent, rank, edge[0], edge[1])
        return len(edges) == n - 1

sol = Solution()
print(sol.validTree(5, [[0,1],[0,4],[1,4],[1,3]]))
print(sol.validTree(4,[[0,1],[2,3]]))
print(sol.validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))
