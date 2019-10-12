class Solution:
    def calc_cost(self, chips, pos):
        cost = 0
        for chip in chips:
            cost += abs(pos - chip) % 2
        return cost

    def minCostToMoveChips(self, chips):
        if not chips:
            return 0
        odds = sum(map(lambda x: 1 if x % 2 == 1 else 0, chips))
        evens = len(chips) - odds
        for pos,_ in enumerate(chips):
            if odds > evens:
                if pos % 2 == 1:
                    return self.calc_cost(chips, pos)
            else:
                if pos % 2 == 0:
                    return self.calc_cost(chips, pos)
        return self.calc_cost(chips, chips[0])

sol = Solution()
print(sol.minCostToMoveChips([6,4,7,8,2,10,2,7,9,7]))#4
print(sol.minCostToMoveChips([2,2,2,3,3]))
print(sol.minCostToMoveChips([1,2,3]))








