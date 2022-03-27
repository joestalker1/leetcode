import math
from collections import defaultdict

class Node:
    def __init__(self):
        self.child = [0,0]
        self.cnt = 0

class Trie:
    def __init__(self, n):
        self.n = n
        self.root = Node()

    def insert(self, num):
        start = self.root
        for i in range(self.n, -1, -1):
            if not start.child[(num >> i) & 1]:
                start.child[(num >> i) & 1] = Node()
            start = start.child[(num >> i) & 1]
            start.cnt += 1

    def remove(self, num):
        start = self.root
        for i in range(self.n, -1,-1):
            start.child[(num >> i) & 1].cnt -= 1
            if start.child[(num >> i) & 1].cnt == 0:
                start.child[(num >> i) & 1] = None
                return
            start = start.child[(num >> i) & 1]

    def max(self, num):
        start = self.root
        maxi = 0
        for i in range(self.n, -1, -1):
            if start.child[1 - ((num >> i) & 1)]:
                maxi += (1 << i)
                start = start.child[1- ((num >> i) & 1)]
            elif start.child[(num >> i) & 1]:
                start = start.child[(num >> i) & 1]

        return maxi



class Solution:
    def dfs(self, cur, g, q, queries, ans, tree, last):
        tree.insert(cur)
        for i in range(len(q[cur])):
            ans[q[cur][i]] = tree.max(queries[q[cur][i]][1])
        for i in range(len(g[cur])):
            ntb = g[cur][i]
            if ntb != last:
                self.dfs(ntb, g, q, queries, ans, tree, cur)
        tree.remove(cur)

    def maxGeneticDifference(self, parents, queries):
        g = defaultdict(list)
        n = len(parents)
        root = 0
        for i in range(n):
            if parents[i] != -1:
                g[parents[i]].append(i)
                #g[i].append(parents[i])
            else:
                root = i
        m = len(queries)
        ans = [0] * m
        q = defaultdict(list)
        for i in range(m):
            q[queries[i][0]].append(i)
        logn = int(math.log2(100000))+1
        tree = Trie(logn)
        self.dfs(root, g,q, queries,ans,tree, -1)
        return ans


sol = Solution()
print(sol.maxGeneticDifference(parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]))



