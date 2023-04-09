import math

class Solution:
    def maxJump(self, stones) -> int:
        if not stones:
            return 0
        if len(stones) <= 3:
            return stones[-1]
        MAX_VAL = 10 ** 9
        stones_num = len(stones)
        back_path_cost = [MAX_VAL] * len(stones)
        for i in range(1,stones_num - 1):
            back_path_cost[i] = [i, stones[-1] - stones[i] + stones[i+1]]
        min_val = math.inf
        j = 0
        for i in range(1, stones_num-1):
            if back_path_cost[i][1] < min_val:
                min_val = min(min_val, back_path_cost[i][1])
                j = i
        return max(stones[-1] - stones[j], stones[j])


sol = Solution()
print(sol.maxJump([0,5,13,14]))#13
