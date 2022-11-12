from collections import defaultdict
import math

class Solution:
    def gridGame(self, grid) -> int:
        if not grid:
            return 0
        pre_sum1 = sum(grid[0])
        pre_sum2 = 0
        m = len(grid[0])
        left_min_cost = math.inf
        for i in range(m):
            pre_sum1 -= grid[0][i]
            #cost of second robot that can go either by 0 row or by 1 row.Choose max one
            left_cost = max(pre_sum2, pre_sum1)
            pre_sum2 += grid[1][i]
            #Update with min left_cost
            left_min_cost = min(left_cost, left_min_cost)
        return left_min_cost

sol = Solution()
print(sol.gridGame([[20,3,20,17,2,12,15,17,4,15],[20,10,13,14,15,5,2,3,14,3]]))#63
print(sol.gridGame([[2,5,4],[1,5,1]]))#4