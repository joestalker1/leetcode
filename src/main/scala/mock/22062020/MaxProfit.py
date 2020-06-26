class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        max_profit = 0
        min_price = float('inf')
        max_price = 0
        for i in range(len(prices)):
            if prices[i] > max_price:
                max_price = prices[i]
            elif prices[i] < min_price:
                min_price = prices[i]
                max_price = prices[i]
            max_profit = max(max_profit, max_price - min_price)
        return max_profit


sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))
print(sol.maxProfit([7,1,5,3,6,4]))
