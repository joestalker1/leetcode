class Solution:
    def mincostTickets(self, days, costs) -> int:
        dayset = set(days)
        def find_min_cost(d, mem):
            if d in mem:
                return mem[d]
            if days[-1] < d:
                return 0
            min_cost = find_min_cost(d + 1, mem)
            if d in dayset:
                #1 day pass
                min_cost = min(costs[0] + min_cost,costs[1] + find_min_cost(d + 7, mem), costs[2] + find_min_cost(d + 30, mem))
            mem[d] = min_cost
            return mem[d]

        return find_min_cost(0, {})


sol = Solution()
print(sol.mincostTickets([1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29], [3,14,50]))#50



