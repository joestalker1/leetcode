import math


class Solution:
    def coinChange(self, coins, amount):
        m = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(1, amount + 1):
            # if there is no coins, then there is infinity ways to make i
            m[0][i] = math.inf
        # go by row
        for c in range(1, len(coins) + 1):
            # for every amount
            for r in range(1, amount + 1):
                # coin's denomination is r
                if coins[c - 1] == r:
                    m[c][r] = 1
                # if coin's denomination is greater r, than take ways from previous coin
                elif coins[c - 1] > r:
                    m[c][r] = m[c - 1][r]
                else:
                    # min: 1) without this coin,2) with this coin
                    m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
        return m[-1][-1] if m[-1][-1] != math.inf else -1


sol = Solution()
print(sol.coinChange([1, 2, 5, 10], 13))
print(sol.coinChange([1, 2, 5, 10], 13))
