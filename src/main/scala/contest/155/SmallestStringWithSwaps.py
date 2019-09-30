from collections import defaultdict

class Solution:
    def smallestStringWithSwaps(self, s, pairs):
        if not s:
            return None
        if len(pairs) == 0:
            return s
        def find(parent, i):
            if parent[i] != i:
                p = find(parent, parent[i])
                parent[i] = p
            return parent[i]

        def union(parent, i, j):
            p1 = find(parent, i)
            p2 = find(parent, j)
            if p1 != p2:
                parent[p1] = p2

        parent = [i for i in range(len(s))]
        for i,j in pairs:
            union(parent, i, j)

        chars = defaultdict(list)
        for i in range(len(s)):
            chars[find(parent, i)].append(s[i])
        for k in chars:
            chars[k].sort()

        res = []
        for i in range(len(s)):
            res.append(chars[find(parent, i)].pop(0))
        return ''.join(res)

sol = Solution()
print(sol.smallestStringWithSwaps("udyyek", [[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]]))#"deykuy"
#print(sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
#print(sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))





