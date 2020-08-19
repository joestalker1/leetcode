class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return None
        right_max = [0] * len(prices)
        right_max[-1] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            right_max[i] = max(prices[i], right_max[i+1])
        max_profit = 0
        for i in range(len(prices)-1):
            max_profit = max(max_profit, right_max[i+1] - prices[i])
        return max_profit




