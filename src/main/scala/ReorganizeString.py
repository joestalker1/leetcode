from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, S):
        if not S:
            return ''
        q = [[-S.count(x), x] for x in set(S)]
        heapq.heapify(q)
        if any(-nc > (len(S) + 1)// 2 for nc,x in q):
            return ''
        res = []
        while len(q) >= 2:
            nc1,x1 = heappop(q)
            nc2,x2 = heappop(q)
            if not res or res[-1] != x1:
                res.extend([x1,x2])
            else:
                res.extend([x2,x1])
            nc1+=1
            nc2 += 1
            if nc1:
                heappush(q, [nc1, x1])
            if nc2:
                heappush(q, [nc2, x2])
        return ''.join(res) + (q[-1][1] if q else '')


sol = Solution()
print(sol.reorganizeString(S = "aaab"))
print(sol.reorganizeString(S = "aab"))





