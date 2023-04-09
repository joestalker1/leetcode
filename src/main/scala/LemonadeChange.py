class Solution:
    def lemonadeChange(self, bills) -> bool:
        if not bills:
            return False
        profit = {5:0,10:0,20:0}
        for bill in bills:
            change = bill - 5
            has_10 = min(change // 10, profit[10])
            profit[10] -= has_10
            change -= 10*has_10
            has_5 = min(change // 5,profit[5])
            profit[5] -= has_5
            change -= 5*has_5
            if change:
                return False
            profit[bill] += 1
        return True