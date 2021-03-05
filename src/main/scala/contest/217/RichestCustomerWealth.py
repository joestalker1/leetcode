class Solution:
    def maximumWealth(self, accounts):
        if len(accounts) == 0 or len(accounts[0])== 0:
            return 0

        max_wealth = 0
        for i in range(len(accounts)):
            row = accounts[i]
            max_wealth = max(max_wealth, sum(row))
        return max_wealth