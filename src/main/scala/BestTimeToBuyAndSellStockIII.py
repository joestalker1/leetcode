class Solution:
    def maxProfit(self, prices) -> int:
        buy_first_stock = prices[0]
        sell_first_stock = 0
        buy_second_stock = -prices[0]
        sell_second_stock = 0
        for price in prices:
            buy_first_stock = min(buy_first_stock,price)
            sell_first_stock = max(sell_first_stock, price - buy_first_stock)
            #pay price min price for second stock
            buy_second_stock = max(buy_second_stock, sell_first_stock - price)
            sell_second_stock = max(sell_second_stock,buy_second_stock + price )
        return sell_second_stock
