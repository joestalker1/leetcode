class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        house_num = len(costs)
        color_num = len(costs[0])
        prev_min_cost = prev_sec_min_cost = prev_min_color = None
        for clr,cost in enumerate(costs[0]):
            if prev_min_cost is None or cost < prev_min_cost:
                prev_sec_min_cost = prev_min_cost
                prev_min_cost = cost
                prev_min_color = clr
            elif prev_sec_min_cost is None or cost < prev_sec_min_cost:
                prev_sec_min_cost = cost

        for h in range(1, house_num):
            min_cost = sec_min_cost = min_color = None
            for clr in range(color_num):
                cost = costs[h][clr]
                if clr == prev_min_color:
                    cost += prev_sec_min_cost
                else:
                    cost += prev_min_cost
                if min_cost is None or cost < min_cost:
                    sec_min_cost = min_cost
                    min_cost = cost
                    min_color = clr
                elif sec_min_cost is None or cost < sec_min_cost:
                    sec_min_cost = cost
            prev_min_cost = min_cost
            prev_sec_min_cost = sec_min_cost
            prev_min_color = min_color
        return prev_min_cost