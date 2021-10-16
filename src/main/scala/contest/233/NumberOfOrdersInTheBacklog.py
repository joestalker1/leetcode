from heapq import heappop,heappush


class Solution:
    def getNumberOfBacklogOrders(self, orders):
        if not orders or len(orders[0]) == 0:
            return 0
        #backlogs
        sell_ord = [] # minimal priority queue
        buy_ord = [] # maximal priority queue
        # 0 is buy, 1 is sell
        for price,amount,t in orders:
            if t == 0:# buy
                while sell_ord and sell_ord[0][0] <= price and amount:
                    price2,amount2 = sell_ord[0]
                    heappop(sell_ord)
                    min_amount = min(amount, amount2)
                    amount -= min_amount
                    amount2 -= min_amount
                    if amount2 > 0:
                        heappush(sell_ord,[price2,amount2])
                if amount > 0:
                    heappush(buy_ord, [-price, amount])
            else:
                while buy_ord and -buy_ord[0][0] >= price and amount:
                    price2,amount2 = buy_ord[0]
                    price2 = -price2
                    heappop(buy_ord)
                    min_amount = min(amount, amount2)
                    amount -= min_amount
                    amount2 -= min_amount
                    if amount2 > 0:
                        heappush(buy_ord, [-price2, amount2])
                if amount > 0:
                    heappush(sell_ord, [price, amount])
        mod = 10 ** 9 + 7
        return (sum([amount for price,amount in sell_ord]) + sum([amount for price,amount in buy_ord])) % mod

sol = Solution()
print(sol.getNumberOfBacklogOrders([[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]))
print(sol.getNumberOfBacklogOrders([[10,5,0],[15,2,1],[25,1,1],[30,4,0]]))


