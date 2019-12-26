from collections import defaultdict
from heapq import heappop,heappush

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        if n == 0 or not flights:
            return -1
        adj_list = defaultdict(list)
        for s,e,w in flights:
            adj_list[s].append((w, e))

        q = [(0,K+1,src)]
        #seen = set()
        while q:
            w,step,u = heappop(q)
            if u == dst:
                return w
            if step > 0:
                for w1,v in adj_list[u]:
                    heappush(q, (w + w1, step - 1, v))
        return -1


sol = Solution()
#print(sol.findCheapestPrice(3,[[0,1,2],[1,2,1],[2,0,10]],1,2, 1))#1
#print(sol.findCheapestPrice(2,[[0,1,2]],1,0,0))# -1
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],0, 2, 0))
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],0, 2, 1))






