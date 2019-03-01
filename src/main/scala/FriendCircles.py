class Solution:
    def find(self, parent, i):
        if parent[i] != -1:
            parent[i] = self.find(parent, parent[i])
        return i

    def union(self, parent, rank, i, j):
        p1 = self.find(parent, i)
        p2 = self.find(parent, j)
        if p1 == p2:
            return
        if rank[p1] > rank[p2]:
            parent[p2] = p1
        elif rank[p2] > rank[p1]:
            parent[p1] = p2
        else:
            parent[p2] = p1
            rank[p1] += 1

    def findCircleNum(self, m) -> int:
        if not m:
            return 0
        parent = [-1] * len(m)
        rank = [0] * len(m)
        for i in range(len(m)):
            for j in range(len(m)):
                if i != j and m[i][j] == 1:
                    self.union(parent, rank, i, j)
        # count groups
        return len(list(filter(lambda x: x == -1, parent)))


sol = Solution()
arr1 = [[1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]]

print(sol.findCircleNum(arr1))

arr2 = [[1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]]
print(sol.findCircleNum(arr2))
