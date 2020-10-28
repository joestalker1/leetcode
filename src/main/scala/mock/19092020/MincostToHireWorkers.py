class Solution:
    def mincostToHireWorkers(self, quality, wage, K):

        def find_min_cost(i, cur):
            if cur == len(wage) or cur == i:
                return 0
            k = quality[i] / quality[cur]
            return min(k * wage[i] + find_min_cost(i, cur + 1), find_min_cost(i, cur + 1))
        min_cost = float('inf')
        for i in range(len(wage)):
            min_cost = min(min_cost, find_min_cost(i, 0))
        return min_cost


