class Solution:
    def __init__(self, price, m, c):
        self.price = price# garment_id, model
        self.m = m
        self.c = c

    def shop(self, money_left, garment_id, memo):
        if money_left < 0:
            return float('-inf')
        if garment_id == self.c:
            return self.m - money_left
        if memo[money_left][garment_id] != -1:
            return memo[money_left][garment_id]
        max_val = float('-inf')
        for model in range(1, self.price[garment_id][0]+ 1):
            max_val = max(max_val, self.shop(money_left - self.price[garment_id][model], garment_id + 1))
        memo[money_left][garment_id] = max_val
        return memo[money_left][garment_id]
    

