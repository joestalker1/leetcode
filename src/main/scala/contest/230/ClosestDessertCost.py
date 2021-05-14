import bisect

class Solution:
    def closestCost(self, baseCosts, toppingCosts, target: int):
        prices = []
        for i in range(len(baseCosts)):
            base = [baseCosts[i]]
            for j in range(len(toppingCosts)):
                new_price = []
                for p in base:
                    new_price.append(p + toppingCosts[j])
                    new_price.append(p + toppingCosts[j] * 2)
                base.extend(new_price)
            prices.extend(base)
        prices.sort()
        i = bisect.bisect_left(prices, target)
        if i == len(prices):
            i -= 1
        if i < len(prices) and prices[i] == target or i == 0:
            return prices[i]
        d1 = abs(prices[i-1] - target)
        d2 = abs(prices[i]-target)
        if d1 == d2:
            return prices[i-1]
        if d1 > d2:
            return prices[i]
        return prices[i-1]


sol = Solution()
print(sol.closestCost([4],[9], 9))#17
print(sol.closestCost([2,3],[4,5,100], 18))#17




