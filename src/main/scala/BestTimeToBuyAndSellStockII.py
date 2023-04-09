class Solution:
    def maxProfit(self, prices) -> int:
        # assert self._maxProfit([7,1,5,3,6,4]) == 7, 'test1'
        # assert self._maxProfit([1,2,3,4,5]) == 4, 'test2'
        # assert self._maxProfit([3,2,1]) == 0, 'test3'
        return self._maxProfit(prices)

    def _maxProfit(self, prices) -> int:
        if len(prices) < 2:
            return 0
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1];
        return max_profit