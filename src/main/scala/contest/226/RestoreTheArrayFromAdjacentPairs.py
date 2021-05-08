from collections import defaultdict

class Solution:
    def restoreArray(self, adjacentPairs):
        m = defaultdict(list)
        for i in range(len(adjacentPairs)):
            a,b = adjacentPairs[i]
            m[a].append(i)
            m[b].append(i)
        v = [v for v,l in m.items() if len(l) == 1]
        q = [v[0]]
        n = len(adjacentPairs) + 1
        seen = set()
        while len(q) < n:
            for i in m[q[-1]]:
                if i in seen:
                    continue
                else:
                    break
            seen.add(i)
            a,b = adjacentPairs[i]
            if a == q[-1]:
                q.append(b)
            else:
                q.append(a)
        return q



sol = Solution()
print(sol.restoreArray([[2,1],[3,4],[3,2]]))
print(sol.restoreArray([[91207,59631],[581,91207],[51465,20358],[-66119,94118],[-7392,72809],[51465,-7392],[-98504,-29411],[-98504,35968],[35968,59631],[94118,20358],[72809,581],[34348,43653],[43653,-29411]]))








