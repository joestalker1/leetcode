class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # assert self._minCostClimbingStairs([10,20,30]) == 20, 'test1'
        # assert self._minCostClimbingStairs([20,10,30]) == 10, 'test2'
        return self._minCostClimbingStairs(cost)

    def _minCostClimbingStairs(self, cost) -> int:
        # if leave the i-step,we will pay cost[i]
        # minimal cost to reach out to the step i.
        dp1 = 0
        dp2 = 0
        # cost to reach to top from i
        for i in range(2, len(cost) + 1):
            min_cost = min(dp1 + cost[i - 1], dp2 + cost[i - 2])
            dp2 = dp1
            dp1 = min_cost
        return dp1

