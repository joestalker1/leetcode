from heapq import heapify,heappop,heappush
import math

class Solution:
    def minStoneSum(self, piles, k: int) -> int:
        if k==0 or not piles:
            return 0
        q = [-pile for pile in piles]
        heapify(q)
        for i in range(k):
            pile = -heappop(q)
            took = math.ceil(pile/ 2)
            heappush(q, -took)
        return -sum(q)


sol = Solution()
print(sol.minStoneSum([5,4,9], 2))