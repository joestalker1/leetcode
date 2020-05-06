from heapq import heappush,heappop,heapify

class Solution:
    def connectSticks(self, sticks):
        if len(sticks) == 1:
            return sticks[0]
        cost = 0
        heapify(sticks)
        while len(sticks) > 1:
            l1 = heappop(sticks)
            l2 = heappop(sticks)
            l = l1+l2
            cost += l
            heappush(sticks, l)
        return cost
