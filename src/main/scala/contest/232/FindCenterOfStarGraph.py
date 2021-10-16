class Solution:
    def findCenter(self, edges):
        if not edges:
            return None
        n = len(edges) + 1
        deg = [0] * n
        for e,v in edges:
            deg[e] += 1
            deg[v] += 1
        for i in range(1,n + 1):
            if deg[i] == n - 1:
                return i
