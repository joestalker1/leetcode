class Solution:
    def twoCitySchedCost(self, costs) -> int:
        n = len(costs)// 2
        city_a = [i for i in range(len(costs))]
        #calculate difference between cost1 - cost2,if cost2 << cost1 it will be at first place.
        city_a.sort(key=lambda i: costs[i][1] - costs[i][0])
        min_cost = 0
        for i in range(len(costs)//2):
            min_cost += costs[city_a[i]][1]
            min_cost += costs[city_a[i + n]][0]
        return min_cost
