class Solution:
    def maxJump(self, stones) -> int:
        if not stones:
            return 0
        if len(stones) < 3:
            return stones[-1]
        max_cost = max(stones[1],stones[2], stones[-1] - stones[-2])
        stones_num = len(stones)
        for i in range(1, stones_num-1):
            max_cost = max(max_cost, stones[min(i+2,stones_num - 1)] - stones[i])
        return max_cost
    