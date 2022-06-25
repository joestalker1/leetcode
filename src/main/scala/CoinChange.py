from math import inf

class Solution:
    def coinChange(self, coins, amount):
        # assert self._coinChange([2,1,1], 3) == 2,'test1'
        # assert self._coinChange([5], 3) == -1, 'test2'
        return self._coinChange(coins, amount)

    def _coinChange(self, coins, amount):
        if not coins or amount <= 0:
            return 0
        coins.sort()
        coin_num = [inf] * (amount + 1)
        for coin in coins:
            if coin > amount:
                break
            coin_num[coin] = 1
        if coin_num[amount] == 1:
            return coin_num[amount]
        for i in range(1, amount + 1):
            if coin_num[amount] != inf:
                continue
            for coin in coins:
                if i < coin:
                    break
                coin_num[i] = min(coin_num[i], coin_num[i - coin] + 1)
        return coin_num[amount] if coin_num[amount] != inf else -1


sol = Solution()
print(sol.coinChange([1, 2, 5, 10], 13))
print(sol.coinChange([1, 2, 5, 10], 13))
